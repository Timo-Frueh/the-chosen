# coding=utf-8

"""
This module holds the Player class.
"""

# The Chosen  Copyright (C) 2021  Timo Früh
# Full copyright notice in main.py

import the_chosen.io as io
from the_chosen.direction_helper import DirectionHelper as Dh


class Player:
    """
    This is the class for the player.
    """

    def __init__(self, player_name, starting_room):
        self.name = player_name
        self.inventory = []
        self.current_room = starting_room
        self.alive = True
        self.kills = 0
        self.victory = False

    def move(self, direction):
        """
        Move the player to a specific direction.

        :param direction: The direction the player wants to move to.
        :type direction: str
        """

        move = direction.lower().strip()
        link = self.current_room.get_link(move)

        if not link and move in Dh.HORIZ_DIRECTIONS:
            io.ch_print("You run head first into a wall and realize: You can't go that way.")
        elif not link and move == Dh.UP:
            io.ch_print("You jump. Nothing happens. Do you expect me to applaud?")
        elif not link and move == Dh.DOWN:
            io.ch_print("You kneel down and examine the floor. There doesn't seem to be a way down.")
        elif not link:
            io.ch_print("You can't go that way.")
        elif not link.isopen():
            io.ch_print(f"The door to the {direction} is closed.")
        else:
            link.print_message(move)
            self.current_room = link.get_other_room(self.current_room)
            self.current_room.describe()

    def look(self):
        """
        Print the description of the room the player is currently in.
        """

        self.get_current_room().describe()

    def talk(self, character):
        """
        Talk to a character.

        :param character: The character the player wants to talk to.
        :type character: Character
        """

        if character.strip() == "":
            user_input = input("Talk to whom? ")
        else:
            user_input = character

        talk_to = user_input.lower().strip()
        character = self.current_room.get_character(talk_to)

        if not self.current_room.get_characters():
            io.ch_print("There is no one here to listen to your beautiful voice.")
        elif not character:
            io.ch_print(f"There is no one called {user_input} here.")
        else:
            character.talk()
            
    def show_inventory(self):
        """
        Print the player's inventory.
        """

        if self.get_inventory():
            io.ch_print("You are carrying:")
            for item in self.get_inventory():
                io.ch_print(f"- {item.get_c_art_name()}")

        else:
            io.ch_print("You are empty-handed.")
    
    def fight(self, character, item):
        """
        Fight a character with an item.

        :param character: The character the player wants to fight.
        :type character: Character

        :param item: The item the player wants to fight with.
        :type item: Item
        """

        if character.strip() == "":
            user_input = input("Fight whom? ")
        else:
            user_input = character
        
        fight = user_input.lower().strip()
        enemy = self.current_room.get_character(fight)

        if enemy and item.strip() == "":
            user_input_2 = input("What do you want to fight with? ")
        elif enemy and item.strip() != "":
            user_input_2 = item
        else:
            user_input_2 = ""
        
        fight_with = user_input_2.lower().strip()
        weapon = self.get_inventory_item(fight_with)

        if not self.current_room.get_characters():
            io.ch_print("There is no one here to fight.")
        elif not enemy:
            io.ch_print(f"There is no one called {user_input} here.")
        elif not weapon:
            io.ch_print(f"You do not have an item called {user_input_2}.")
        else:
            enemy.fight(weapon, self)
    
    def take(self, item):
        """
        Take an item.

        :param item: The item the player wants to take.
        :type item: Item
        """

        if item.strip() == "":
            user_input = input("What do you want to take? ")
        else:
            user_input = item
        
        take = user_input.lower().strip()
        item = self.current_room.get_item(take)

        if not self.current_room.get_items():
            io.ch_print("There is nothing here to take.")
        elif not item:
            io.ch_print(f"There is no item called {user_input} here.")
        else:
            self.current_room.remove_item(item)
            self.add_to_inventory(item)
            io.ch_print("Taken.")

    def drop(self, item):
        """
        Drop an item out of the inventory.

        :param item: The item the player wants to drop.
        :type item: Item
        """

        if item.strip() == "":
            user_input = input("What do you want to drop? ")
        else:
            user_input = item
        
        drop = user_input.lower().strip()
        item = self.get_inventory_item(drop)

        if not self.inventory:
            io.ch_print("You do not have anything to drop.")
        elif not item:
            io.ch_print(f"You do not have an item called {user_input}.")
        else:
            self.remove_from_inventory(item)
            self.current_room.add_item(item)
            io.ch_print("Dropped.")
    
    def hug(self, character):
        """
        Hug a character.

        :param character: The character the player wants to hug.
        :type character: Character
        """

        if character.strip() == "":
            user_input = input("Hug whom? ")
        else:
            user_input = character

        hug = user_input.lower().strip()
        character = self.current_room.get_character(hug)

        if not self.current_room.get_characters():
            io.ch_print("There is no one here to receive your comforting embrace.")
        elif not character:
            io.ch_print(f"There is no one called {user_input} here.")
        else:
            character.hug()
                
    def open_door(self, direction, key):
        """
        Open a door.

        :param direction: The direction the desired door is to.
        :type direction: str

        :param key: The key to use to open the door.
        :type key: Item
        """

        if direction.strip() == "":
            user_input = input("Open door to which direction? ")
        else:
            user_input = direction

        open_door = user_input.lower().strip()
        open_with = key.lower().strip()
        door = self.current_room.get_link(open_door)
        key = self.get_inventory_item(open_with)

        if open_door not in Dh.HORIZ_DIRECTIONS:
            io.ch_print("You need to specify a direction so I know which door you mean.")
        elif not door:
            io.ch_print(f"There is no door to the {user_input}.")
        elif key:
            door.unlock_door(key)
            door.open_door()
        else:
            door.open_door()

    def unlock_door(self, direction, key):
        """
        Unlock a door.

        :param direction: The direction the desired door is to.
        :type direction: str

        :param key: The key to use to unlock the door.
        :type key: Item
        """
        
        if direction.strip() == "":
            user_input = input("Unlock door to which direction? ")
        else:
            user_input = direction

        unlock_door = user_input.lower().strip()
        door = self.current_room.get_link(unlock_door)

        if door and key.strip() == "":
            user_input_2 = input("Which key do you want to use? ")
        elif door and key.strip() != "":
            user_input_2 = key
        else:
            user_input_2 = ""

        unlock_with = user_input_2.lower().strip()
        key = self.get_inventory_item(unlock_with)
        
        if unlock_door not in Dh.HORIZ_DIRECTIONS:
            io.ch_print("You need to specify a direction so I know which door you mean.")
        elif not door:
            io.ch_print(f"There is no door to the {user_input}.")
        elif not key:
            io.ch_print(f"You do not have an item called {user_input_2}.")
        else:
            door.unlock_door(key)

    def close_door(self, direction, key):
        """
        Close a door.

        :param direction: The direction the desired door is to.
        :type direction: str

        :param key: The key to use to close the door.
        :type key: Item
        """

        if direction.strip() == "":
            user_input = input("Open door to which direction? ")
        else:
            user_input = direction

        close_door = user_input.lower().strip()
        close_with = key.lower().strip()
        door = self.current_room.get_link(close_door)
        key = self.get_inventory_item(close_with)

        if close_door not in Dh.HORIZ_DIRECTIONS:
            io.ch_print("You need to specify a direction so I know which door you mean.")
        elif not door:
            io.ch_print(f"There is no door to the {user_input}.")
        elif key:
            door.close_door()
            door.lock_door(key)
        else:
            door.close_door()

    def lock_door(self, direction, key):
        """
        Lock a door.

        :param direction: The direction the desired door is to.
        :type direction: str

        :param key: The key to use to lock the door.
        :type key: Item
        """

        if direction.strip() == "":
            user_input = input("Lock door to which direction? ")
        else:
            user_input = direction

        lock_door = user_input.lower().strip()
        door = self.current_room.get_link(lock_door)

        if door and key.strip() == "":
            user_input_2 = input("Which key do you want to use? ")
        elif door and key.strip() != "":
            user_input_2 = key
        else:
            user_input_2 = ""

        lock_with = user_input_2.lower().strip()
        key = self.get_inventory_item(lock_with)
        
        if lock_door not in Dh.HORIZ_DIRECTIONS:
            io.ch_print("You need to specify a direction so I know which door you mean.")
        elif not door:
            io.ch_print(f"There is no door to the {user_input}.")
        elif door.islocked():
            io.ch_print(f"You do not have an item called {user_input_2}.")
        else:
            door.lock_door(key)

    def get_inventory(self):
        """
        Return the player's inventory.

        :return: The player's inventory.
        :rtype: list
        """

        return self.inventory

    def get_inventory_item(self, name):
        """
        Return a specifit item from the inventory.

        :param name: The item's name.
        :type name: str

        :return: The desired item.
        :rtype: Item
        """

        for item in self.inventory:
            if name.lower().strip() in item.get_aliases():
                return item

    def add_to_inventory(self, item):
        """
        Add an item to the inventory.

        :param item: The item to add to the inventory.
        :type item: Item
        """

        self.inventory.append(item)

    def remove_from_inventory(self, item):
        """
        Remove an item from the inventory.

        :param item: The item to remove from the inventory.
        :type item: Item
        """

        self.inventory.remove(item)

    def get_name(self):
        """
        Return the player's name.

        :return: The player's name.
        :rtype: str
        """

        return self.name

    def get_current_room(self):
        """
        Return the player's current room.

        :return: The player's current room.
        :rtype: Room
        """

        return self.current_room

    def isalive(self):
        """
        Check whether the player is alive or not.

        :return: A boolean showing whether the player is alive or not.
        :rtype: bool
        """

        return self.alive

    def die(self):
        """
        Kill the player.
        """

        self.alive = False

    def get_kills(self):
        """
        Return the player's kill count.

        :return: The player's kill count.
        :rtype: int
        """

        return self.kills

    def add_kill(self):
        """
        Add a kill to the player's kill count.
        """

        self.kills += 1

    def haswon(self):
        """
        Check whether the player has won the game yet.

        :return: A boolean showing whether the player has won the game yet.
        :rtype: bool
        """

        return self.victory

    def win(self):
        """
        Let the player win the game.
        """

        self.victory = True
