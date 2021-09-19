# HacktivityCon 2021 Write-up: Movie Marathon - Scripting

## Task details:
Heard some bozo bragging about knowing more movies than anyone else? Could you put him in his place, please!

<br>

## Write up:

The first thing was to look at the output of the terminal after connecting via netcat.

```log
    __  ___           _         __  ___                 __  __              
   /  |/  /___ _   __(_)__     /  |/  /___ __________ _/ /_/ /_  ____  ____ 
  / /|_/ / __ \ | / / / _ \   / /|_/ / __ `/ ___/ __ `/ __/ __ \/ __ \/ __ \
 / /  / / /_/ / |/ / /  __/  / /  / / /_/ / /  / /_/ / /_/ / / / /_/ / / / /
/_/  /_/\____/|___/_/\___/  /_/  /_/\__,_/_/   \__,_/\__/_/ /_/\____/_/ /_/ 
                                                                            
You think you know movies more than I do? If you can send me any 5 cast members for each movie that I mention, I'll reward you.
e.g. The Avengers (2012-04-25)
Chris Evans; Robert Downey Jr.; Mark Ruffalo; Chris Hemsworth; Scarlett Johansson



> All About Eve (1950-10-06)
* 
```

As can be seen from the above output, the task can be decomposed into the following steps:
1. Communicate with a server via netcat
1. Get movie title and release date
1. Find any 5 names of the actors playing in it
1. Send back 5 actor names as one string with separator ';'
1. Repeat until you get a flag

<br>

### 1. Communication via netcat
Because **netcat** (**nc**) is an utility for reading from and writing to network connections using TCP or UDP, it can be implemented as a simple python function using `socket` module.

In function **`netcat`** I establish connection, decode received data from bytes to string and try to find characters indicating that this string contains the data about movie. If there are such a data, then the function **`get_answer`** is called which will return 5 actor names as one string with separator. I also added logic for printing in terminal received and response data for better look and logging function **`save_to_disk`** so the flag would be saved if anything happens to the terminal or connection and it closes.

```python
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
```


### 2. Get movie title and release date
Function **`get_movie_str`** is needed in order to ensure that the received text from server contains information about movie. This is done by searching for specific character **`> `** indicating start of the movie info and extracting this substring to the end of the text, returned string has to be stripped of all control characters such as **`\n`** as well.

```python
def get_movie_str(text):
	""" Find substring containing movie and release date in response sent by bot """
	movie_str = ''
	movie_str = text[text.find('> '):]
	return movie_str[1:].strip()
```

Because of the specifics of the movie search algorithms on many web sites with such information, there were needed only movie title and release year. Function **`get_title_date`** extracts this information from already precomputed string received from server.

```python
def get_title_date(movie_str):
	""" Get movie title and release year """
	title = movie_str[:movie_str.find(' (')]
	year = movie_str[movie_str.find('(')+1:movie_str.find(')')]
	return title, year
```


### 3. Find any 5 names of the actors playing in it
In order to solve this problem the following solutions were probed:
- Scraping movie database sites in order to get information
- Using movie database sites API
  - OMDb API - The Open Movie Database
  - IMDb API
  - TMDB API - The Movie Database

Scraping websites and IMDB API had an issue with getting relevant search results, thus it sometimes replied wrong actors for the desired movie. With OMDB API everything was perfect except one thing: the number of actors it retrieved was maximum 3 - not enough for this task.
TMDB was the best choice: it gave everything you need to solve this task with minimum code.
The **`get_movie_id`** function returns movie id for the specified title for which the release date completely matches the date specified by server.

```python
def get_movie_id(title, release_date):
	search = tmdb.Search()
	response = search.movie(query=title)

	movie_id = -1
	for result in search.results:
		if result.get('release_date') == release_date:
			movie_id = result['id']
	return movie_id
```


### 4. Send back 5 actor names as one string with separator ';'
The **`get_cast_str`** makes a request for the TMDB API using movie id from the step 3, retrieves 5 names and then contatenates them using specified separator.

```python
def get_cast_str(movie_id, max_actors=5):
	""" Prepare answer for netcat with cast names as single string with separator ';' """
	film = tmdb.Movies(movie_id)
	credits = film.credits()
	cast = credits.get('cast')
	cast_names = []
	for actor in islice(cast, 0, max_actors):
		cast_names.append(actor.get('name'))
	return '; '.join(cast_names)
```


### 5. Repeat until you get a flag
Steps 1-4 are repeated until the flag is received and connection is closed. To complete this challenge it requires to get an answer for 30 movies.

In order to test this solution pipeline without connecting to the server the **`test`** function was implemented.

```python
def test():
	received_data = '> The Avengers (2012-04-25)'
	expected = 'Robert Downey Jr.; Chris Evans; Scarlett Johansson; Jeremy Renner; Mark Ruffalo'
	movie_str = get_movie_str(received_data)
	print('movie_str:', movie_str)
	print('expected_answer:', expected)
	print('received_answer:', get_answer(movie_str))
```

<br>

The full source code and log file with client-server dialog and flag can be found [here](https://github.com/requroku/CTFWriteUps/tree/main/2021-09-H@cktivityCon/Movie-Marathon).
