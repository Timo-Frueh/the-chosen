# coding=utf-8

# The Chosen  Copyright (C) 2021  Timo Früh
# Full copyright notice in main.py

from the_chosen.entity import Entity


class Item(Entity):

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
        self.kill_messages = {}
        self.requirements = {"kills": 0}
        self.no_req_message = None
    
    def set_def_kill_message(self, kill_message):
        self.kill_messages["def"] = kill_message

    def set_kill_message(self, character_name, kill_message):
        self.kill_messages[character_name] = kill_message
    
    def print_kill_message(self, character):
        if character.get_name() in self.kill_messages:
            print(self.kill_messages[character.get_name()])
        elif self.kill_messages["def"]:
            print(f"{self.kill_messages['def']}, killing {character.get_the_name()}.")
        else:
            print(f"You kill {character.get_the_name()} with {self.the_name}.")

    def set_kills_req(self, kills):
        self.requirements["kills"] = kills
    
    def req_are_met(self, player):
        met = True

        if player.get_kills() < self.requirements["kills"]:
            met = False

        return met
    
    def set_no_req_message(self, no_req_message):
        self.no_req_message = no_req_message
    
    def print_no_req_message(self):
        if self.no_req_message:
            print(self.no_req_message)
        else:
            print("You do not yet meet this weapon's requirements and therefore lose the fight.\nYou die ...")


class Artifact(Weapon):

    def __init__(self, art, item_name, initial_room):
        super().__init__(art, item_name)
        self.initial_room = initial_room
        self.initial_description = None

    def describe_initial(self):
        print(f"{self.c_art_name} is here, {self.initial_description}")

    def get_initial_description(self):
        return self.initial_description

    def set_initial_description(self, initial_description):
        self.initial_description = initial_description

    def get_initial_room(self):
        return self.initial_room


class Artifacts(Artifact):
    def __init__(self, item_name, initial_room):
        super().__init__("the", item_name, initial_room)

    def describe(self):
        print(f"{self.c_the_name} are here, {self.description}")

    def describe_initial(self):
        print(f"{self.c_the_name} are here, {self.initial_description}")
