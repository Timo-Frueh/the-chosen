# coding=utf-8

# The Chosen  Copyright (C) 2021  Timo Früh
# Full copyright notice in main.py

from the_chosen.entity import Entity


class Item(Entity):

    # print a line describing the character
    def describe(self):
        print(f"{self.c_art_name} is here, {self.description}")


class Key(Item):
    def __init__(self, art, name):
        super().__init__(art, name)
        self.unlock_message = None
        self.lock_message = None

    def set_unlock_message(self, unlock_message):
        self.unlock_message = unlock_message
    
    def print_unlock_message(self):
        if self.unlock_message:
            print(self.unlock_message)
        else:
            print("You unlock the door.")

    def set_lock_message(self, lock_message):
        self.lock_message = lock_message

    def print_lock_message(self):
        if self.lock_message:
            print(self.lock_message)
        else:
            print("You lock the door.")


class Weapon(Item):
    def __init__(self, art, name):
        super().__init__(art, name)
        self.kill_message = None
    
    def set_kill_message(self, kill_message):
        self.kill_message = kill_message
    
    def print_kill_message(self, character):
        if self.kill_message:
            print(f"{self.kill_message}, killing {character.get_the_name()}.")
        else:
            print(f"You kill {character.get_the_name()} with {self.the_name}.")


class Artifact(Weapon):

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
