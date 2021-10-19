class Room:
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.characters = []
        self.items = []

    def describe(self):
        print(self.name)

        for n in range(0, len(self.name)-1):
            print("¯", end="")
        print("¯")

        print(self.description)

        for character in self.characters:
            character.describe()

        for item in self.items:
            item.describe()

        for direction in self.linked_rooms:
            print(f"There is a door to the {direction}.")

    def get_desc(self):
        return self.description

    def set_desc(self, new_description):
        self.description = new_description

    def get_name(self):
        return self.name

    def get_linked_rooms(self):
        return self.linked_rooms

    def link_room(self, direction, room):
        self.linked_rooms[direction] = room

    def get_characters(self):
        return self.characters

    def get_character(self, name):
        for character in self.characters:
            if character.name.lower().replace(" ", "") == name:
                return character

    def add_character(self, character):
        self.characters.append(character)

    def remove_character(self, character):
        self.characters.remove(character)

    def get_items(self):
        return self.items

    def get_item(self, name):
        for item in self.items:
            if item.name.lower().replace(" ", "") == name:
                return item

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)
