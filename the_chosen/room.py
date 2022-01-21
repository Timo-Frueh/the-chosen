# coding=utf-8

"""
This module holds the Room class.
"""

# The Chosen  Copyright (C) 2021  Timo Früh
# Full copyright notice in main.py


class Room:
    """
    This is the base class for rooms, which make up the world the player can move through.
    """

    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.links = {}
        self.doors = {}
        self.ladders = {}
        self.illusory_walls = {}
        self.characters = []
        self.items = []

    def describe(self):
        """
        Print a long description of the room.
        """

        print(self.name)

        for _ in range(0, len(self.name) - 1):
            print("¯", end="")
        print("¯")

        print(self.description)

        for character in self.characters:
            character.describe()

        for item in self.items:
            try:
                if item.get_initial_room() is self:
                    item.describe_initial()
                else:
                    item.describe()
            except AttributeError:
                item.describe()

        self.print_doors()
        self.print_ladders()

    def print_doors(self):
        """
        Print all the connecting doors.
        """

        if len(self.doors) == 1:
            for direction in self.doors:
                print(f"There is a door to the {direction}.")

        elif len(self.doors) == 2:
            directions = []
            for direction in self.doors:
                directions.append(direction)
            print(f"There are doors to the {directions[0]} and {directions[1]}.")

        elif len(self.doors) == 3:
            directions = []
            for direction in self.doors:
                directions.append(direction)
            print(f"There are doors to the {directions[0]}, {directions[1]} and {directions[2]}.")

        elif len(self.doors) == 4:
            print("There are doors to all directions.")

    def print_ladders(self):
        """
        Print all connecting ladders.
        """

        if len(self.ladders) == 1:
            for direction in self.ladders:
                print(f"There is a ladder leading {direction}.")
        elif len(self.ladders) == 2:
            print("There is a ladder leading up and down.")

    def init_links(self):
        """
        Initialise all connecting links, sorting them into doors, ladders and illusory walls.
        """
        for direction in self.links:
            if type(self.links[direction]).__name__ == "Door":
                self.doors[direction] = self.links[direction]

        for direction in self.links:
            if type(self.links[direction]).__name__ == "Ladder":
                self.ladders[direction] = self.links[direction]

        for direction in self.links:
            if type(self.links[direction]).__name__ == "IllusoryWall":
                self.illusory_walls[direction] = self.links[direction]

    def get_desc(self):
        """
        Return the room's description.

        :return: The room's description.
        :rtype: str
        """

        return self.description

    def set_desc(self, new_description):
        """
        Set the room's description.

        :param new_description: The room's description.
        :type new_description: str
        """

        self.description = new_description

    def get_name(self):
        """
        Return the room's name.

        :return: The room's name.
        :rtype: str
        """

        return self.name

    def add_link(self, direction, link):
        """
        Add a link to the room.

        :param direction: The direction the link is connecting at.
        :type direction: str

        :param link: The link connecting at the given direction.
        :type link: Link
        """

        self.links[direction] = link
        self.init_links()

    def get_link(self, direction):
        """
        Get a link from direction.

        :param direction: The direction the desired link is to.
        :type direction: str

        :return: The desired link, if there is one to the specified direction.
        """

        try:
            return self.links[direction]
        except KeyError:
            pass

    def get_characters(self):
        """
        Return all the characters in the room.

        :return: All the characters in the room.
        :rtype: list
        """

        return self.characters

    def get_character(self, search):
        """
        Check whether a character exists in a room.

        :param search: The name of the desired character.
        :type search: str

        :return: The desired character.
        """

        for character in self.characters:
            if search.lower().strip() in character.get_aliases():
                return character

    def add_character(self, character):
        """
        Add a character to the room.

        :param character: The character to add.
        :type character: Character
        """

        self.characters.append(character)

    def remove_character(self, character):
        """
        Remove a character from a room.

        :param character: The character to remove.
        :type character: Character
        """

        self.characters.remove(character)

    def get_items(self):
        """
        Return the items in a room.

        :return: A list of all the items in the room.
        :rtype: list
        """

        return self.items

    def get_item(self, name):
        """
        Get an item by name.

        :param name: The name of the desired item.
        :type name: str

        :return: The desired item, if it exists in the room.
        """

        for item in self.items:
            if name.lower().strip() in item.get_aliases():
                return item

    def add_item(self, item):
        """
        Add an item to the room.

        :param item: The item to add.
        :type item: Item
        """

        self.items.append(item)

    def remove_item(self, item):
        """
        Remove an item from the room.

        :param item: The item to remove.
        :type item: Item
        """

        self.items.remove(item)
