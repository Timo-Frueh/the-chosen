# coding=utf-8

"""
This module holds the Mainloop class.
"""

# The Chosen  Copyright (C) 2022  Timo Früh
# Full copyright notice in __main__.py

import the_chosen.io as io
from the_chosen.direction_helper import DirectionHelper as Dh
from the_chosen.resource_helper import ResourceHelper as Rh
from the_chosen.rpginfo import RPGInfo


class Mainloop:
    """
    This is the class containing the mainloop function.
    """

    @staticmethod
    def mainloop(player):
        """
        This is the mainloop method, in which the user's commands are processed over and over, until the game ends.
        """

        commands_list = Rh.read_resource("commands_list.txt")

        alive = True

        victory = False

        while alive and not victory:

            io.ch_print("")
            user_input = io.cmd_input()
            
            command = user_input.lower().strip()

            command_key = command.split(" ")[0]

            if command in ["commands", "help", "?"]:
                io.ch_print(commands_list)

            elif command in Dh.DIRECTIONS:
                player.move(command)

            elif command in ["look", "l"]:
                player.look()

            elif command_key == "talk":

                talk_input = io.interpret_single(command, "talk", [" to "])

                player.talk(talk_input)

            elif command in ["inventory", "i", "backpack"]:
                player.show_inventory()

            elif command_key == "fight":

                fight_input = io.interpret_double(command, "fight", "with", [", "])

                player.fight(character=fight_input[0], item=fight_input[1])

            elif command_key == "take":

                take_input = io.interpret_single(command, "take")

                player.take(take_input)

            elif command_key == "drop":

                drop_input = io.interpret_single(command, "drop", [])

                player.drop(drop_input)

            elif command_key == "hug":

                hug_input = io.interpret_single(command, "hug")

                player.hug(hug_input)

            elif command_key == "open":
                open_with_input = io.interpret_double(command, "open", "with", [" the ", " door"])
                player.open_door(direction=open_with_input[0], key=open_with_input[1])

            elif command_key == "close":
                close_with_input = io.interpret_double(command, "close", "with", [" the ", " door"])
                player.close_door(direction=close_with_input[0], key=close_with_input[1])

            elif command_key == "unlock":
                unlock_input = io.interpret_double(command, "unlock", "with", [" the ", " door"])
                player.unlock_door(direction=unlock_input[0], key=unlock_input[1])

            elif command_key == "lock":
                lock_input = io.interpret_double(command, "lock", "with", [" the ", " door"])
                player.lock_door(direction=lock_input[0], key=lock_input[1])

            elif command_key in ["scream", "shout"]:
                io.ch_print("Aaaaaaaaaaaaargh!")

            elif command in ["quit", "exit"]:

                confirm = io.ch_input("Do you really wish to leave the game? (y is affermative) ").strip()

                if confirm in ["Y", "y"]:
                    alive = False

            elif command == "":
                pass

            else:
                io.ch_print(f"I do not know what you meant by {user_input}.")

            if not player.isalive():
                alive = False

            if player.haswon():
                victory = True

        if victory:
            io.ch_print("\nCongratulations! You have been victorious and thereby beaten the game!\n")

        if player.get_kills() == 0:
            io.ch_print("You vanquished not a single enemy during the game.")
        elif player.get_kills() == 1:
            io.ch_print("You vanquished 1 enemy during the game.")
        elif player.get_kills() > 1:
            io.ch_print(f"You vanquished {player.get_kills()} enemies during the game.")

        io.ch_print("")

        if victory:
            RPGInfo.credits()

            io.ch_print("")

        io.ch_input("[Hit enter to exit.]")
