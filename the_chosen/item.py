# coding=utf-8

"""
This module holds the Item class and all its subclasses.

Classes:

    Item
    Key
    Weapon
    Artifact
    Artifacts
"""

# The Chosen  Copyright (C) 2021-2023  Timo Früh
# Full copyright notice in __main__.py

import the_chosen.io as io
from the_chosen.entity import Entity


class Item(Entity):
    """
    This is the class for Items, wich can be picked up, dropped and can have a message to print when something is
    killed with it.
    """
    def __init__(self, art, name):
        super().__init__(art, name)
        self.kill_messages = {}

    def describe(self):
        """
        Describe the item.
        """

        io.ch_print(f"{self.c_art_name} is here, {self.description}")

    def set_def_kill_message(self, kill_message):
        """
        Set the default message to be printed when something is killed with with this item.

        :param kill_message: The item's default kill message to be set.
        :type kill_message: str
        """

        self.kill_messages["def"] = kill_message

    def set_kill_message(self, character_name, kill_message):
        """
        Set the message to be printed when a certain enemy is killed with this item.

        :param character_name: The name of the character the kill message is for.
        :type character_name: str

        :param kill_message: The kill message for characters of the name {character_name}
        :type kill_message: str
        """
        self.kill_messages[character_name] = kill_message

    def print_kill_message(self, character):
        """
        Print the correct kill message for when a certain character is killed.

        :param character: The character the message should be printed for.
        :type character: Character
        """

        if character.get_name() in self.kill_messages:
            io.ch_print(self.kill_messages[character.get_name()])
        elif "def" in self.kill_messages:
            io.ch_print(f"{self.kill_messages['def']}, killing {character.get_the_name()}.")
        else:
            io.ch_print(f"You kill {character.get_the_name()} with {self.the_name}.")

    def req_are_met(self, player):
        """
        Determine whether the requirements for this item are met by a specified player.
        Always returns true, as items don't have requirements.

        :param player: The player the check should be made for.
        :type player: Player

        :return: Whether the requirements for this item are met. (Always true for normal items)
        :rtype: bool
        """

        return True


class Key(Item):
    """
    This is the class for keys, which can be used to unlock and lock doors.
    """
    def __init__(self, art, name):
        super().__init__(art, name)
        self.unlock_message = None
        self.lock_message = None

    def set_unlock_message(self, unlock_message):
        """
        Set a message to print when a door is unlocked by this key.

        :param unlock_message: The unlock message to set.
        :type unlock_message: str
        """

        self.unlock_message = unlock_message
    
    def print_unlock_message(self):
        """
        Print the unlock message if there is one, print a default one otherwhise.
        """

        if self.unlock_message:
            io.ch_print(self.unlock_message)
        else:
            io.ch_print("You unlock the door.")

    def set_lock_message(self, lock_message):
        """
        Set a message to print when a door is locked by this key.

        :param lock_message: The lock message to set.
        :type lock_message: str
        """
        self.lock_message = lock_message

    def print_lock_message(self):
        """
        Print the lock message if there is one, print a default one otherwhise.
        """

        if self.lock_message:
            io.ch_print(self.lock_message)
        else:
            io.ch_print("You lock the door.")


class Weapon(Item):
    """
    This is the class for weapons, which have requirements that the player has to have in order to use them.
    """
    def __init__(self, art, name):
        super().__init__(art, name)
        self.requirements = {"kills": 0}
        self.no_req_message = None

    def set_kills_req(self, kills):
        """
        Set a kill requirement.

        :param kills: The kills needed to use a weapon.
        :type kills: int
        """

        self.requirements["kills"] = kills
    
    def req_are_met(self, player):
        """
        Check whether a player meets the requirements.

        :param player: The player to check.
        :type player: Player
        """

        met = True

        if player.get_kills() < self.requirements["kills"]:
            met = False

        return met
    
    def set_no_req_message(self, no_req_message):
        """
        Set the message to be displayed if the requirements are not met.

        :param no_req_message: The message to display.
        :type no_req_message: str
        """

        self.no_req_message = no_req_message
    
    def print_no_req_message(self):
        """
        Print the no_req_message or a default one if there is none.
        """

        if self.no_req_message:
            io.ch_print(self.no_req_message)
        else:
            io.ch_print("You do not yet meet this weapon's requirements and therefore lose the fight.\nYou die ...")


class Artifact(Weapon):
    """
    This is the class for artifact weapons which have a different description if in their initial room.
    """
    def __init__(self, art, item_name, initial_room):
        super().__init__(art, item_name)
        self.initial_room = initial_room
        self.initial_description = None

    def describe_initial(self):
        """
        Print the initial description.
        """

        io.ch_print(f"{self.c_art_name} is here, {self.initial_description}")

    def get_initial_description(self):
        """
        Return the initial description.

        :return: The initial description of the artifact weapon.
        :rtype: str
        """

        return self.initial_description

    def set_initial_description(self, initial_description):
        """
        Set the weapon's initial description which is displayen when it lies in its initial room.

        :param initial_description: The artifact weapon's initial description.
        :type initial_description: str
        """

        self.initial_description = initial_description

    def get_initial_room(self):
        """
        Return the initial room of an artifact weapon.

        :return: The artifact weapon's initial room.
        :rtype: Room
        """

        return self.initial_room


class Artifacts(Artifact):
    """
    This is the class for dual artifact weapons.
    """

    def __init__(self, item_name, initial_room):
        super().__init__("the", item_name, initial_room)

    def describe(self):
        """
        Print the description of the weapons.
        """

        io.ch_print(f"{self.c_the_name} are here, {self.description}")

    def describe_initial(self):
        """
        Print the initial description.
        """

        io.ch_print(f"{self.c_the_name} are here, {self.initial_description}")
