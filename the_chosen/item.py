# coding=utf-8

# The Chosen  Copyright (C) 2021  Timo Früh
# Full copyright notice in main.py

from the_chosen.entity import Entity

class Item (Entity):

    # define constructor and the five object attributes
    def __init__(self, art, item_name):
        super().__init__(art, item_name)

    # print a line describing the character
    def describe(self):
        print(f"{self.c_art_name} is here, {self.description}")


class Artifact(Item):

    # define constructor, set the article to "the", add an initial room and a initial description
    # (which is to be displayed if the item is lying in that initial room)
    def __init__(self, art, item_name, initial_room):
        super().__init__(art, item_name)
        self.initial_room = initial_room
        self.initial_description = None

    # print a line describing the item when lying in the initial room
    def describe_initial(self):
        print(f"{self.c_art_name} is here, {self.initial_description}")

    # getters and setters
    def get_initial_description(self):
        return self.initial_description

    def set_initial_description(self, initial_description):
        self.initial_description = initial_description

    def get_initial_room(self):
        return self.initial_room


class Artifacts(Artifact):
    def __init__(self, item_name, initial_room):
        super().__init__("the", item_name, initial_room)

    # print a line describing the items
    def describe(self):
        print(f"{self.c_the_name} are here, {self.description}")

    # print a line describing the items when lying in the initial room
    def describe_initial(self):
        print(f"{self.c_the_name} are here, {self.initial_description}")
