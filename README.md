# The Chosen: At Nights End

This is a short Zork-like text-adventure I wrote.

Your objective is to find a pair of legendary swords and kill an evil king with them.

## How to install

### macOS, Linux

To install directly from the latest release, use:
~~~ shell
sudo curl -L https://github.com/Timo-Frueh/the-chosen/releases/latest/download/the-chosen -o /usr/local/bin/the-chosen
sudo chmod a+rx /usr/local/bin/the-chosen
~~~

Or, alternatively, with`wget`
~~~ shell
sudo wget https://github.com/Timo-Frueh/the-chosen/releases/latest/download/the-chosen -O /usr/local/bin/the-chosen
sudo chmod a+rx /usr/local/bin/the-chosen
~~~

### Windows, macOS, Linux

You can also just download the ZIP-file or tarball from the latest release and install with `setup.py` manually.

## How to play

There are multiple commands you can use to interact with the game world. 
This following list can also be displayed in-game by typing `help` and pressing `enter` afterwards.

### Command list

~~~ text
north     :  move north
east      :  move east
south     :  move south
west      :  move west
up        :  move up
down      :  move down
look      :  look at your surroundings
talk      :  talk to someone in the room
inventory :  show what you are carrying
fight     :  fight someone
take      :  put something into your inventory
drop      :  drop something in your inventory
hug       :  hug someone
quit      :  quit the game -> NOTE: you will not be able to restore the game later
help      :  show this list
~~~

### Shortcuts

There are also some shortcuts:

~~~ text
l    : look
i    : inventory
~~~

### Positional commands

There are also positional commands:

`talk`, `fight`, `take`, `drop` and `hug` are positional commands.

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
