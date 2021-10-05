# TastelessCTF 2021 Write-up. [game] Skull Island

## Description:
Find the flag in the eye of the danger (in the game)!

https://ctf.tasteless.eu/tasteless-shores

<br>

| Value | Difficulty   |
| ----- | ------------ |
| 443   | Medium       |

<br>

## Write-up:
In this challenge we're given a game [Tasteless Shores](https://ctf.tasteless.eu/tasteless-shores) and the flags are have to be found inside it.

After logging in and running around for a bit, it was obvious that challenge description gives a hint for where we have to find a flag. And the flag must be in one of the skull eyes.

However, it was not so easy to get there. Character must have a boat to travel to different islands, otherwise it will die.
According to organizers hint, before this challenge another have to be done, where we acquire a boat. I was not able to solve previous challenge, but found a workaround.

First step was to look at the provided files, one of them is `tasteless-shores.pck`, which is a resource pack file for [Godot Engine](https://docs.godotengine.org/en/latest/index.html). After searching for some time, it became clear that `.pck` file can not only contain textures, models and music, but as well as client-sided scripts.

After searching for some time more, I found [Godot Reverse Engineering Tools](https://github.com/bruvzg/gdsdecomp) project on github. These tools were able to extract `.pck` file contents as well as decompile `.gdc` and compile `.gd` script files. 
In the `tasteless-shores/game/player` directory was a compiled script called `player.gdc`.

```log
tasteless-shores.pck
    ├───.import
    ├───addons
    │   └───EminMultiMesh
    │       ├───dock
    │       ├───icon
    │       └───multimeshnode
    ├───assets
    │   ├───characters
    │   ├───materials
    │   ├───textures
    │   │   ├───darkcliff-Rock035_2K-JPG
    │   │   ├───Grass004_1K-JPG
    │   │   ├───grass_01
    │   │   │   ├───grass_01
    │   │   │   ├───grass_02
    │   │   │   └───grass_03
    │   │   ├───Gravel002_2K-JPG
    │   │   ├───kenney
    │   │   │   ├───cartographypack
    │   │   │   │   ├───PNG
    │   │   │   │   │   ├───Default
    │   │   │   │   │   └───Retina
    │   │   │   │   ├───Spritesheet
    │   │   │   │   ├───Textures
    │   │   │   │   └───Vector
    │   │   │   ├───kenney_prototypetextures
    │   │   │   │   ├───PNG
    │   │   │   │   │   ├───Dark
    │   │   │   │   │   ├───Green
    │   │   │   │   │   ├───Light
    │   │   │   │   │   ├───Orange
    │   │   │   │   │   ├───Purple
    │   │   │   │   │   └───Red
    │   │   │   │   └───Vector
    │   │   │   └───particlePack_1.1
    │   │   │       ├───PNG (Black background)
    │   │   │       │   └───Rotated
    │   │   │       └───PNG (Transparent)
    │   │   │           └───Rotated
    │   │   ├───Rock016_1K-JPG
    │   │   └───Sand1k
    │   └───weapons
    ├───game
    │   ├───items
    │   ├───net
    │   ├───player
    │   ├───screen
    │   ├───ui
    │   └───unit
    ├───island
    │   ├───home
    │   │   └───obj
    │   ├───melee_island
    │   ├───tasteless_shores
    │   │   ├───obj
    │   │   └───quests
    │   └───town
    │       └───obj
    │           ├───castle
    │           ├───fort
    │           ├───gallow
    │           └───merchants
    ├───music
    ├───objects
    │   ├───chest
    │   └───fire
    └───shipwreck
```

After decompilation and looking through the script contents it became clear that after certain requirements are met `marker` dictionary is appended with new flag variable set to `true`, then the chest spawns, after interacting with this chest flag is revealed.

```gd
var marker = {
	"FLAG_EYES":true, 
}

...

func _on_Water_water_entered():
	if "FLAG_BOAT" in marker:
		_setBoat(true)
	else :
		drowning = true
		if Client.player == self:
			Ui.show_note("I can't swim")
```

I decided to add the variable `FLAG_BOAT` and set it to true, so that when in water I could swim. After doing so I compiled the script and then compiled the whole `.pck` file. Then, after logging into the game I discovered that simply setting this flag to true did't eliminate the problem of drowning, because the game was still thinking that character can't swim even if the boat is spawned. However, the speed was enough to get from one island to another without dying.

After reaching the skull island it was needed to get to one of the eyes and find the flag. Game physics allowed to climb almost vertically so it was possible to get there relatively easy.

And so, the chest was in the left eye:

![skull island](./img/Skull-Island-1.png)

<br>

The flag:
```log
tstlss{do_you_S33_me_now?}
```
