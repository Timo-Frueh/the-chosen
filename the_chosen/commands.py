# coding=utf-8

# The Chosen  Copyright (C) 2021  Timo Früh
# Full copyright notice in main.py

from the_chosen.character import Character, Enemy, Friend


class Commands:

    # make a list of all possible commands
    commands = {"north     ": "  move north",
                "east      ": "  move east",
                "south     ": "  move south",
                "west      ": "  move west",
                "up        ": "  move up",
                "down      ": "  move down",
                "look      ": "  look at your surroundings",
                "talk      ": "  talk to someone in the room",
                "inventory ": "  show what you are carrying",
                "fight     ": "  fight someone",
                "take      ": "  put something into your inventory",
                "drop      ": "  drop something in your inventory",
                "hug       ": "  hug someone",
                "quit      ": "  quit the game -> NOTE: you will not be able to restore the game later",
                "help      ": "  show this list"}

    # define the help method: print all possible commands
    @classmethod
    def print_commands(cls):
        for command in cls.commands:
            print(f"{command}:{cls.commands[command]}")

    # define the movement command
    @staticmethod
    def movement(player, direction):

        # move the player in the desired direction
        player.move(direction)

        # print the details of the new room
        player.get_current_room().describe()

    # define the look command
    @staticmethod
    def look(player):

        # print the details of the current room
        player.get_current_room().describe()

    # define the talk command
    @staticmethod
    def talk(player, whom):

        # if there is anyone in the current room do the following
        if player.get_current_room().get_characters():

            # if there was no input specifying a character ask for one
            if not whom:
                user_input = input("Talk to whom? ")
            else:
                user_input = whom

            # make the user input all lowercase and strip it of whitespaces at beginning and end
            talk_to = user_input.lower().strip()

            # get the character in the room the player wants to talk to
            character = player.get_current_room().get_character(talk_to)

            # if this character exists and is in the current room talk to them
            if character:
                character.talk()

            # if this character doesn't exist or is not in the current room print a message
            else:
                print(f"There is no one called {user_input} here.")

        # if there is no-one in the current room print a message
        else:
            print("There is no one here to listen to your beautiful voice.")

    # define the inventory command
    @staticmethod
    def show_inventory(player):

        # if the player has anything in their inventory print all items (including capital articles) in a bulletlist
        if player.get_inventory():
            print("You are carrying:")
            for item in player.get_inventory():
                print(f"- {item.get_name_w_cap_art()}")

        # if the player doesn't have anything print a message
        else:
            print("You are empty-handed.")

    # define the fight method
    @staticmethod
    def fight(player, whom, item):

        # if there is anyone in the current room do the following
        if player.get_current_room().get_characters():

            # if there was no input specifying the character ask for one
            if not whom:
                user_input = input("Fight whom? ")
            else:
                user_input = whom

            # make the user input all lowercase and strip it of whitespaces at beginning and end
            fight = user_input.lower().strip()

            # get the character in the room the player wants to fight
            enemy = player.get_current_room().get_character(fight)

            # if this character exists do the following
            if enemy:

                # if there was no input specifying the weapon ask for one
                if not item:
                    scnd_input = input("What do you want to fight with? ")
                else:
                    scnd_input = item

                # make the user input all lowercase and strip it of whitespaces at beginning and end
                fight_with = scnd_input.lower().strip()

                # get the weapon the player wants to fight with
                weapon = player.get_inventory_item(fight_with)

                # if this weapon exists and is in the players inventory do the following
                if weapon:

                    # start the fight
                    player.get_current_room().get_character(fight).fight(weapon, player)

                # if this weapon doesn't exist or is not in the players inventory display a message
                else:
                    print(f"You do not have a {scnd_input}.")

            # if this character doesn't exist or is not in the current room display a message
            else:
                print(f"There is no one called {user_input} here.")

        # if there is no-one in the room to fight display a message
        else:
            print("There is no one here to fight.")

    # define the take command
    @staticmethod
    def take(player, what):

        # if there is anything in the room to take do the following
        if player.get_current_room().get_items():

            # if there was no input specifying the item ask for one
            if not what:
                user_input = input("What do you want to take? ")
            else:
                user_input = what

            # make the user input all lowercase and strip it of whitespaces at beginning and end
            take = user_input.lower().strip()

            # get the item the player wants to take
            item = player.get_current_room().get_item(take)

            # if this item exists and is in the current room do the following
            if item:

                # remove the item from the current room
                player.get_current_room().remove_item(item)

                # add the item to the players inventory
                player.add_to_inventory(item)

                # print a message that the item was taken
                print("Taken.")

            # if this item doesn't exist or is not in the current room print a message
            else:
                print(f"There is no item called {user_input} here.")

        # if there isn't anything in the room to take print a message
        else:
            print("There is nothing here to take.")

    # define the drop command
    @staticmethod
    def drop(player, what):

        # if there is anything in the players inventory do the following
        if player.get_inventory():

            # if there was no input specifying the item ask for one
            if not what:
                user_input = input("What do you want do drop? ")
            else:
                user_input = what

            # make the user input all lowercase and strip it of whitespaces at beginning and end
            drop = user_input.lower().strip()

            # get the item the player wants to drop
            item = player.get_inventory_item(drop)

            # if this item exists and is in the players inventory do the following
            if item:

                # remove the item from the players inventory
                player.remove_from_inventory(item)

                # add the item to the current room
                player.get_current_room().add_item(item)

                # print a message that the item was dropped
                print("Dropped.")

            # if this item doesn't exist or is not in the players inventory print a message
            else:
                print(f"You do not have a {user_input}.")

        # if there isn't anything in the inventory to drop print a message
        else:
            print("You do not have anything to drop.")

    # define the hug command
    @staticmethod
    def hug(player, whom):

        # if there is anyone in the room to hug do the following
        if player.get_current_room().get_characters():

            # if there was no input specifying the character ask for one
            if not whom:
                user_input = input("Hug whom? ")
            else:
                user_input = whom

            # make the user input all lowercase and strip it of whitespaces at beginning and end
            hug = user_input.lower().strip()

            # get the character the player wants to hug
            character = player.get_current_room().get_character(hug)

            # if this character exists and is in the current room do the following
            if character:

                # if the character is a friend hug them
                if isinstance(character, Friend):
                    character.hug()

                # if the character is an enemy print a message
                elif isinstance(character, Enemy):
                    print("You wouldn't want to hug this malicious creature.")

                # if the character is any other character type print a message
                elif isinstance(character, Character):
                    print("I doubt they'd appreciate that.")

            # if this character doesn't exist or is not in the current room print a message
            else:
                print(f"There is no one called {user_input} here.")

        # if there is no-one in the room to hug print a message
        else:
            print("There is no one here to receive your comforting embrace.")

    # define the quit command
    @staticmethod
    def quit():

        # ask for confirmation on quitting and strip the input of whitespaces at beginning and end
        confirm = input("Do you really whish to leave the game? (y is affermative) ").strip()

        # if the quitting was confirmed return true
        if confirm in ["Y", "y"]:
            return True

        # if the quitting was not confirmed return false
        else:
            return False
