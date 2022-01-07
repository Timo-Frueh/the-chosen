# coding=utf-8

"""
This module holds the Commands class.
"""

# The Chosen  Copyright (C) 2021  Timo Früh
# Full copyright notice in main.py


class Commands:
    """
    This class is for printing all available commands.
    """

    # make a list of all possible commands
    commands = {"north      ": "  move north",
                "east       ": "  move east",
                "south      ": "  move south",
                "west       ": "  move west",
                "up         ": "  move up",
                "down       ": "  move down",
                "look       ": "  look at your surroundings",
                "talk       ": "  talk to someone in the room",
                "inventory  ": "  show what you are carrying",
                "fight      ": "  fight someone",
                "take       ": "  put something into your inventory",
                "drop       ": "  drop something in your inventory",
                "hug        ": "  hug someone",
                "open/close ": "  open/close a door",
                "(un-)lock  ": "  lock/unlock a door",
                "scream     ": "  scream",
                "quit       ": "  quit the game -> NOTE: you will not be able to restore the game later",
                "help       ": "  show this list"}

    # define the help method: print all possible commands
    @classmethod
    def print_commands(cls):
        """
        Print all available commands.
        """
        
        for command in cls.commands:
            print(f"{command}:{cls.commands[command]}")
