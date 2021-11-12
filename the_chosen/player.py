# coding=utf-8

# The Chosen  Copyright (C) 2021  Timo Früh
# Full copyright notice in main.py

class Player:

    # define constructor and four object attributes
    def __init__(self, player_name, starting_room):
        self.name = player_name
        self.inventory = []
        self.current_room = starting_room
        self.kills = 0

    # move to a room to the direction
    def move(self, direction):

        # check all links of the current room, move if there is a room to the desired direction and
        # print special messages for vertical and hidden links
        if direction in self.current_room.get_links():
            self.current_room = self.current_room.get_links()[direction]
        elif direction in self.current_room.get_vertical_links():
            print(f"You climb {direction} the ladder.\n")
            self.current_room = self.current_room.get_vertical_links()[direction]
        elif direction in self.current_room.get_hidden_links():
            print(f"As you lay your hand upon the {direction} wall, you pass through it and emerge on the other side.\n")
            self.current_room = self.current_room.get_hidden_links()[direction]
        elif direction in ["north", "east", "south", "west"]:
            print("You run head first into a wall and realize: You can't go that way.\n")
        elif direction == "up":
            print("You jump. Nothing happens. What did you expect?\n")
        elif direction == "down":
            print("You kneel down and examine the floor. There doesn't seem to be a way down.\n")
        else:
            print("You can't go that way.\n")

    # getters and setters
    def get_inventory(self):
        return self.inventory

    def get_inventory_item(self, name):
        for item in self.inventory:
            if item.get_name().lower().replace(" ", "") == name.lower().replace(" ", ""):
                return item

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def remove_from_inventory(self, item):
        self.inventory.remove(item)

    def get_name(self):
        return self.name

    def get_current_room(self):
        return self.current_room

    def get_kills(self):
        return self.kills

    def add_kill(self):
        self.kills += 1
