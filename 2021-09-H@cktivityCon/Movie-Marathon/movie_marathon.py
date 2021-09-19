import socket
import tmdbsimple as tmdb
from itertools import islice


def get_movie_str(text):
	""" Find substring containing movie and release date in response sent by bot """
	movie_str = ''
	movie_str = text[text.find('> '):]
	return movie_str[1:].strip()


def get_title_date(movie_str):
	""" Get movie title and release year """
	title = movie_str[:movie_str.find(' (')]
	year = movie_str[movie_str.find('(')+1:movie_str.find(')')]
	return title, year


def get_movie_id(title, release_date):
	search = tmdb.Search()
	response = search.movie(query=title)

	movie_id = -1
	for result in search.results:
		if result.get('release_date') == release_date:
			movie_id = result['id']
	return movie_id


def get_cast_str(movie_id, max_actors=5):
	""" Prepare answer for netcat with cast names as single string with separator ';' """
	film = tmdb.Movies(movie_id)
	credits = film.credits()
	cast = credits.get('cast')
	cast_names = []
	for actor in islice(cast, 0, max_actors):
		cast_names.append(actor.get('name'))
	return '; '.join(cast_names)


def get_answer(movie_str):
	title, release_date = get_title_date(movie_str)
	movie_id = get_movie_id(title, release_date)
	answer = get_cast_str(movie_id)
	return answer


def save_to_disk(data, filename='./movie_marathon.log'):
	with open(filename, "a", encoding='utf-8') as f:
		f.write(data)


def netcat(host, port):
    nc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    nc.connect((host, int(port)))

    movie_num = 0
    while True:
        enc_data = nc.recv(4096*2)
        if not enc_data:
            break

        received_data = enc_data.decode()
        print(received_data)
        save_to_disk(received_data)
        movie_str = get_movie_str(received_data)
        if movie_str:
        	response = get_answer(movie_str)
        	save_to_disk(response + '\n')
        	print(response)
        	nc.sendall(response.encode())
        	movie_num += 1
    nc.close()

    print('movies:', movie_num)
    save_to_disk('\nmovies to complete challenge:' + str(movie_num))


def test():
	received_data = '> The Avengers (2012-04-25)'
	expected = 'Robert Downey Jr.; Chris Evans; Scarlett Johansson; Jeremy Renner; Mark Ruffalo'
	movie_str = get_movie_str(received_data)
	print('movie_str:', movie_str)
	print('expected_answer:', expected)
	print('received_answer:', get_answer(movie_str))


def main():
	host = 'challenge.ctf.games'
	port = 31260
	netcat(host, port)


if __name__ == '__main__':
	tmdb.API_KEY = 'YOUR_API_KEY'
	main()
