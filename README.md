# The Chosen: At Nights End

This is a short Zork-like text-adventure I wrote.

Your objective is to find a pair of legendary swords and kill an evil king with them.

## How to install

### macOS (with Homebrew)

1. Tap my brew-repo: `brew tap https://github.com/tifrueh/homebrew-mytap`

2. Install with `brew install the-chosen`

### Windows, macOS, Linux

1. You can download the ZIP-file or tarball from the latest release and install with `pip` manually.

2. You can also download the ZIP-file or tarball from the latest release and run the game directly with `python` from the entry script `the-chosen.py`

## How to play

There are multiple commands you can use to interact with the game world. 
This following list can also be displayed in-game by typing `help` and pressing `enter` afterwards.

### Command list

~~~ text
north      :  move north
east       :  move east
south      :  move south
west       :  move west
up         :  move up
down       :  move down
look       :  look at your surroundings
talk       :  talk to someone in the room
inventory  :  show what you are carrying
fight      :  fight someone
take       :  put something into your inventory
drop       :  drop something in your inventory
hug        :  hug someone
open/close :  open/close a door
(un-)lock  :  (un-)lock a door
scream     :  scream
quit       :  quit the game -> NOTE: you will not be able to restore the game later
help       :  show this list
~~~

_Note: To unlock and open (or close and lock) a door direcly, use `open {direction} with {key}` 
(or `close {direction} with {key}`)_

### Shortcuts

There are also some shortcuts:

~~~ text
l    : look
i    : inventory
~~~

### Positional commands

There are also positional commands:

`talk`, `fight`, `take`, `drop`, `hug`, `open`, `close`, `lock` and `unlock` are positional commands.

An example `talk` command:

~~~ text
> talk stranger                  -> talk to a NPC named "stranger"
~~~

An example `fight` command:

~~~ text
> fight stranger with sword     -> fight a NPC named "stranger" with a weapon called "sword"
~~~

You can also just input a positional command as you would input a normal one and the game will ask you for the parameters.

Have fun!
