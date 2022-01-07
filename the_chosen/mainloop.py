# coding=utf-8

# The Chosen  Copyright (C) 2021  Timo Früh
# Full copyright notice in main.py

from the_chosen.commands import Commands as Cmd
from the_chosen.direction_helper import DirectionHelper as Dh
from the_chosen.input_interpreter import InputInterpreter
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

        alive = True

        victory = False

        while alive and not victory:

            print("")
            user_input = input("> ")

            command = user_input.lower().strip()

            if command in ["commands", "help", "?"]:
                Cmd.print_commands()

            elif command in Dh.DIRECTIONS:
                player.move(command)

            elif command in ["look", "l"]:
                player.look()

            elif "talk to" in command:

                talk_to_input = InputInterpreter.interpret_single(command, "talk to")

                player.talk(talk_to_input)

            elif "talk" in command:

                talk_input = InputInterpreter.interpret_single(command, "talk")

                player.talk(talk_input)

            elif command in ["inventory", "i", "backpack"]:
                player.show_inventory()

            elif "fight" in command:

                fight_input = InputInterpreter.interpret_double(command, "fight", "with", [", "])

                player.fight(character=fight_input[0], item=fight_input[1])

            elif "take" in command:

                take_input = InputInterpreter.interpret_single(command, "take")

                player.take(take_input)

            elif "drop" in command:

                drop_input = InputInterpreter.interpret_single(command, "drop", [])

                player.drop(drop_input)

            elif "hug" in command:

                hug_input = InputInterpreter.interpret_single(command, "hug")

                player.hug(hug_input)

            elif "open" in command:
                open_with_input = InputInterpreter.interpret_double(command, "open", "with", [" the ", " door"])
                player.open_door(direction=open_with_input[0], key=open_with_input[1])

            elif "close" in command:
                close_with_input = InputInterpreter.interpret_double(command, "close", "with", [" the ", " door"])
                player.close_door(direction=close_with_input[0], key=close_with_input[1])

            elif "unlock" in command:
                unlock_input = InputInterpreter.interpret_double(command, "unlock", "with", [" the ", " door"])
                player.unlock_door(direction=unlock_input[0], key=unlock_input[1])

            elif "lock" in command:
                lock_input = InputInterpreter.interpret_double(command, "lock", "with", [" the ", " door"])
                player.lock_door(direction=lock_input[0], key=lock_input[1])

            elif command in ["quit", "exit"]:

                confirm = input("Do you really whish to leave the game? (y is affermative) ").strip()

                if confirm in ["Y", "y"]:
                    alive = False

            elif command == "":
                pass

            else:
                print(f"I do not know what you meant by {user_input}.")

            if not player.isalive():
                alive = False

            if player.haswon():
                victory = True

        if victory:
            print("\nCongratulations! You have been victorious and thereby beaten the game!\n")

        if player.get_kills() == 0:
            print("You vanquished not a single enemy during the game.")
        elif player.get_kills() == 1:
            print("You vanquished 1 enemy during the game.")
        elif player.get_kills() > 1:
            print(f"You vanquished {player.get_kills()} enemies during the game.")

        print("")

        if victory:
            RPGInfo.credits()

            print("")

        input("[Hit enter to exit.]")
