# coding=utf-8

# The Chosen  Copyright (C) 2021  Timo Früh
# Full copyright notice in main.py


class Room:

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

        if len(self.ladders) == 1:
            for direction in self.ladders:
                print(f"There is a ladder leading {direction}.")
        elif len(self.ladders) == 2:
            print("There is a ladder leading up and down.")

    def init_links(self):

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
        return self.description

    def set_desc(self, new_description):
        self.description = new_description

    def get_name(self):
        return self.name

    def add_link(self, direction, door):
        self.links[direction] = door
        self.init_links()

    def get_link(self, direction):
        try:
            return self.links[direction]
        except KeyError:
            pass

    def get_characters(self):
        return self.characters

    def get_character(self, search):
        for character in self.characters:
            if search.lower().strip() in character.get_aliases():
                return character

    def add_character(self, character):
        self.characters.append(character)

    def remove_character(self, character):
        self.characters.remove(character)

    def get_items(self):
        return self.items

    def get_item(self, name):
        for item in self.items:
            if name.lower().strip() in item.get_aliases():
                return item

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)
