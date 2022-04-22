# coding=utf-8

"""
This module holds the Character class and all its subclasses.

Classes:

    Character
    Stranger
    Friend
    Enemy
    Miniboss
    Endboss
    Mob
"""

# The Chosen  Copyright (C) 2022  Timo Früh
# Full copyright notice in main.py

import the_chosen.io as io
from the_chosen.entity import Entity


class Character(Entity):
    """
    This is the class for normal characters, which cannot be fought.
    """

    def __init__(self, art, character_name):
        super().__init__(art, character_name)
        self.conversations = []
        self.con_counter = 0
        self.hug_message = None

    def describe(self):
        """
        Describe the character.
        """

        io.ch_print(f"You see {self.art_name}, {self.description}")

    def talk(self):
        """
        Talk to the character.
        """

        if len(self.conversations) == 0:
            io.ch_print(f"{self.c_the_name} doesn't want to talk to you.")
        elif self.con_counter < len(self.conversations):
            io.ch_print(f"[{self.c_the_name}]: \n{self.conversations[self.con_counter]}")
        elif self.con_counter >= len(self.conversations):
            io.ch_print(f"[{self.c_the_name}]: \n{self.conversations[-1]}")

        self.con_counter += 1

    def fight(self, weapon, player):  # pylint: disable=unused-argument
        """
        Fight the character (only prints that the character doesn't want to fight).

        :param weapon: The weapon used by the player to fight this character.
        :type weapon: Item

        :param player: The player who fights the character.
        :type player: Player
        """

        io.ch_print(f"{self.name} does not want to fight you.")

    def hug(self):
        """
        Hug the character. Prints the hug message or a default one if there is none.
        """

        if self.hug_message:
            io.ch_print(self.hug_message)
        else:
            io.ch_print("I doubt they'd appreciate that.")

    # getters and setters
    def get_conversation(self):
        """
        Return the character's conversations.

        :return: The character's conversations list.
        :rtype: list
        """

        return self.conversations

    def add_conversation(self, new_conversation):
        """
        Add a new conversation to the conversations list.

        :param new_conversation: The conversation to be added.
        :type new_conversation: str
        """

        self.conversations.append(new_conversation)

    def set_hug_message(self, new_hug_message):
        """
        Set the character's hug message.

        :param new_hug_message: The hug message to be set.
        :type new_hug_message: str
        """

        self.hug_message = new_hug_message


class Stranger(Character):
    """
    This is the class for strangers, which do not have a name and can either be deadly or not when fought.
    """

    def __init__(self, art, class_name, deadly):
        super().__init__(art, class_name)
        self.deadly = deadly

    def fight(self, weapon, player):
        """
        Fight the stranger, kill the player if the stranger was deadly, kill the stranger otherwhise.

        :param weapon: The weapon used by the player to fight this stranger.
        :type weapon: Item

        :param player: The player who fights the character.
        :type player: Player
        """

        if self.deadly:
            io.ch_print(f"{self.c_the_name} didn't wish you harm. But you already started the fight. You lose ...\nYou die ...")
            player.die()

        else:
            io.ch_print(f"You kill {self.c_the_name}.\nThis wasn't right ... You feel sorry for {self.c_the_name}.")
            player.get_current_room().remove_character(self)


class Friend(Character):
    """
    This is the class for friends, which cannot be fought and hug the player back by default.
    """
    def __init__(self, character_name):
        super().__init__("", character_name)

    def hug(self):
        """
        Hug the friend. Prints the hug message or that the friend hugs the player back if there is none.
        """

        if self.hug_message:
            io.ch_print(self.hug_message)
        else:
            io.ch_print(f"{self.name} hugs you back.")

    def fight(self, weapon, player):
        """
        Fight the friend. Prints that the player cannot fight a friend.

        :param weapon: The weapon used by the player to fight this friend.
        :type weapon: Item

        :param player: The player who fights the friend.
        :type player: Player
        """

        io.ch_print("You wouldn't want to hurt a friend, would you?")


class Enemy(Character):
    """
    This is the class for enemies, which have weaknesses and can be killed with those.
    """

    def __init__(self, art, character_name):
        super().__init__(art, character_name)
        self.weaknesses = []
        self.kill_messages = {}

    def fight(self, weapon, player):
        """
        Fight the enemy. Kill the player if weapon requirements are not met or weapon is not a weakness, otherwhise
        kill the enemy.

        :param weapon: The weapon used by the player to fight this enemy.
        :type weapon: Item

        :param player: The player who fights the enemy.
        :type player: Player
        """

        if weapon in self.weaknesses and weapon.req_are_met(player):

            weapon.print_kill_message(self)

            player.get_current_room().remove_character(self)

            player.add_kill()

        elif not weapon.req_are_met(player):
            weapon.print_no_req_message()
            player.die()
        else:
            self.print_kill_message(weapon)
            player.die()

    def hug(self):
        """
        Hug the enemy. Prints the hug message or that the player wouldn't want to hug the enemy if there is none.
        """

        if self.hug_message:
            io.ch_print(self.hug_message)
        else:
            io.ch_print("You wouldn't want to hug this malicious creature.")

    # getters and setters
    def get_weaknesses(self):
        """
        Return the enemy's weaknesses.
        
        :return: The enemy's weaknesses list.
        :rtype: list
        """

        return self.weaknesses

    def add_weakness(self, new_weakness):
        """
        Add a new weakness to the enemy.

        :param new_weakness: The weakness to be added.
        :type new_weakness: Item
        """

        self.weaknesses.append(new_weakness)

    def set_def_kill_message(self, message):
        """
        Set the default message to be printed when the enemy kills the player.

        :param message: The default kill message.
        :type message: str
        """

        self.kill_messages["def"] = message

    def set_kill_message(self, item_name, message):
        """
        Set the message to be printed when the enemy kills the player while they wield a certain item.

        :param item_name: The name of the item that the kill message is for.
        :type item_name: str

        :param message: The kill message for items of the name {item_name}.
        :type message: str
        """

        self.kill_messages[item_name] = message

    def print_kill_message(self, item):
        """
        Print the correct kill message for when a certain item is wielded.

        :param item: The item that the message should be printed for.
        :type item: Item
        """

        if item.get_name() in self.kill_messages:
            io.ch_print(self.kill_messages[item.get_name()])
        elif "def" in self.kill_messages:
            io.ch_print(self.kill_messages["def"])
        else:
            io.ch_print(f"{self.c_the_name} lands a fatal blow.\nYou die ...")


class Miniboss(Enemy):
    """
    This is the class for minibosses, which have a normal name.

    (This class doesn't do much at the moment, but will be extended in the future.)
    """

    def __init__(self, character_name):
        super().__init__("", character_name)


class Endboss(Enemy):
    """
    This is the class for endbosses, which have a title and end the game when defeated.
    """

    def __init__(self, character_name, title):
        super().__init__("", character_name)
        self.title = title
        self.the_title = f"the {self.title}"
        self.c_the_title = f"The {self.title}"
        self.add_alias(self.title)
        self.add_alias(self.the_title)
        self.add_alias(f"{self.name} {self.title}")
        self.add_alias(f"{self.name} {self.the_title}")

    def describe(self):
        """
        Describe the endboss.
        """

        io.ch_print(f"You see {self.name}, the {self.title}, {self.description}")

    def fight(self, weapon, player):
        """
        Fight the endboss. Calls the fight method of the enemy class but ends the game when the fight is won.

        :param weapon: The weapon used by the player to fight this endboss.
        :type weapon: Item

        :param player: The player who fights the endboss.
        :type player: Player
        """
        super().fight(weapon, player)
        if player.isalive():
            player.win()


class Mob(Enemy):
    """
    This is the class for mobs, which are the most common enemy class.

    (This class doesn't to much at the moment, but might be expanded in the future.)
    """

    def describe(self):
        """
        Describe the mob.
        """

        io.ch_print(f"You see {self.art_name}, looking malevolently at you.")

    def talk(self):
        """
        Talk to the mob.
        """

        io.ch_print(f"[The {self.name}]: \n*unintelligible bestial sounds*")
