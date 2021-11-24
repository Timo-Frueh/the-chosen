# coding=utf-8

# The Chosen  Copyright (C) 2021  Timo Früh
# Full copyright notice in main.py

class Player:

    # define constructor and four object attributes
    def __init__(self, player_name, starting_room):
        self.name = player_name
        self.inventory = []
        self.current_room = starting_room
        self.alive = True
        self.kills = 0
        self.victory = False

    # move to a room to the direction
    def move(self, direction):

        # check all links of the current room, move if there is a room to the desired direction and
        # print special messages for vertical and hidden links
        if direction in self.current_room.get_doors():
            self.current_room = self.current_room.get_doors()[direction]
        elif direction in self.current_room.get_ladders():
            print(f"You climb {direction} the ladder.\n")
            self.current_room = self.current_room.get_ladders()[direction]
        elif direction in self.current_room.get_ill_walls():
            print(f"As you lay your hand upon the {direction} wall, you pass through it and emerge on the other side.\n")
            self.current_room = self.current_room.get_ill_walls()[direction]
        elif direction in ["north", "east", "south", "west"]:
            print("You run head first into a wall and realize: You can't go that way.\n")
        elif direction == "up":
            print("You jump. Nothing happens. What did you expect?\n")
        elif direction == "down":
            print("You kneel down and examine the floor. There doesn't seem to be a way down.\n")
        else:
            print("You can't go that way.\n")
        
        self.current_room.describe()


    # look around
    def look(self):

        # print the details of the current room
        self.get_current_room().describe()

    # talk to someone
    def talk(self, whom):

        # if there is anyone in the current room do the following
        if self.get_current_room().get_characters():

            # if there was no input specifying a character ask for one
            if not whom:
                user_input = input("Talk to whom? ")
            else:
                user_input = whom

            # make the user input all lowercase and strip it of whitespaces at beginning and end
            talk_to = user_input.lower().strip()

            # get the character in the room the player wants to talk to
            character = self.get_current_room().get_character(talk_to)

            # if this character exists and is in the current room talk to them
            if character:
                character.talk()

            # if this character doesn't exist or is not in the current room print a message
            else:
                print(f"There is no one called {user_input} here.")

        # if there is no-one in the current room print a message
        else:
            print("There is no one here to listen to your beautiful voice.")

    # show the players inventory
    def show_inventory(self):

        # if the player has anything in their inventory print all items (including capital articles) in a bulletlist
        if self.get_inventory():
            print("You are carrying:")
            for item in self.get_inventory():
                print(f"- {item.get_name_w_cap_art()}")

        # if the player doesn't have anything print a message
        else:
            print("You are empty-handed.")

    # fight someone with something
    def fight(self, whom, item):

        # if there is anyone in the current room do the following
        if self.get_current_room().get_characters():

            # if there was no input specifying the character ask for one
            if not whom:
                user_input = input("Fight whom? ")
            else:
                user_input = whom

            # make the user input all lowercase and strip it of whitespaces at beginning and end
            fight = user_input.lower().strip()

            # get the character in the room the player wants to fight
            enemy = self.get_current_room().get_character(fight)

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
                weapon = self.get_inventory_item(fight_with)

                # if this weapon exists and is in the players inventory do the following
                if weapon:

                    # start the fight
                    self.get_current_room().get_character(fight).fight(weapon, self)

                # if this weapon doesn't exist or is not in the players inventory display a message
                else:
                    print(f"You do not have a {scnd_input}.")

            # if this character doesn't exist or is not in the current room display a message
            else:
                print(f"There is no one called {user_input} here.")

        # if there is no-one in the room to fight display a message
        else:
            print("There is no one here to fight.")

    # take something
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

    # drop something
    def drop(self, what):

        # if there is anything in the players inventory do the following
        if self.get_inventory():

            # if there was no input specifying the item ask for one
            if not what:
                user_input = input("What do you want do drop? ")
            else:
                user_input = what

            # make the user input all lowercase and strip it of whitespaces at beginning and end
            drop = user_input.lower().strip()

            # get the item the player wants to drop
            item = self.get_inventory_item(drop)

            # if this item exists and is in the players inventory do the following
            if item:

                # remove the item from the players inventory
                self.remove_from_inventory(item)

                # add the item to the current room
                self.get_current_room().add_item(item)

                # print a message that the item was dropped
                print("Dropped.")

            # if this item doesn't exist or is not in the players inventory print a message
            else:
                print(f"You do not have a {user_input}.")

        # if there isn't anything in the inventory to drop print a message
        else:
            print("You do not have anything to drop.")

    # hug someone
    def hug(self, whom):

        # if there is anyone in the room to hug do the following
        if self.get_current_room().get_characters():

            # if there was no input specifying the character ask for one
            if not whom:
                user_input = input("Hug whom? ")
            else:
                user_input = whom

            # make the user input all lowercase and strip it of whitespaces at beginning and end
            hug = user_input.lower().strip()

            # get the character the player wants to hug
            character = self.get_current_room().get_character(hug)

            # if this character exists and is in the current room do the following
            if character:

                # hug the character
                character.hug()

            # if this character doesn't exist or is not in the current room print a message
            else:
                print(f"There is no one called {user_input} here.")

        # if there is no-one in the room to hug print a message
        else:
            print("There is no one here to receive your comforting embrace.")

    def pass_through_link(self, link):
        if link in self.current_room.get_doors().values():
            if link.isopen():
                self.current_room == link.get_other_room(self.current_room)
            else:
                print("This door is closed.")
        else:
            raise Exception("This door doesn't connect to the player's current room.")

        if link in self.current_room.get_ladders().values():
            self.current_room = link.get_other_room(self.current_room)
        else:
            raise Exception("This ladder doesn't connect to the player's current room.")
        
        if link in self.current_room.get_ill_walls().values():
            self.current_room = link.get_other_room(self.current_room)
        else:
            raise Exception("This illusory wall doesn't connect to the player's current room.")

    # getters and setters
    def get_inventory(self):
        return self.inventory

    def get_inventory_item(self, name):
        for item in self.inventory:
            if name.lower().strip() in item.get_aliases():
                return item

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def remove_from_inventory(self, item):
        self.inventory.remove(item)

    def get_name(self):
        return self.name

    def get_current_room(self):
        return self.current_room

    def isalive(self):
        return self.alive

    def die(self):
        self.alive = False

    def get_kills(self):
        return self.kills

    def add_kill(self):
        self.kills += 1

    def haswon(self):
        return self.victory
    
    def win(self):
        self.victory = True
