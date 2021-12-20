# coding=utf-8

# The Chosen  Copyright (C) 2021  Timo Früh
# Full copyright notice in main.py

from the_chosen.entity import Entity


class Character(Entity):

    # define constructor and the three opject attributes
    def __init__(self, art, character_name):
        super().__init__(art, character_name)
        self.conversation = None
        self.hug_message = None

    # print a line describing the character
    def describe(self):
        print(f"You see {self.name}, {self.description}")

    # talk to the character
    def talk(self):

        # if a conversation is set print it along with the characters name
        # if none is set print a message that the character doesn't want to talk to you
        if self.conversation:
            print(f"[{self.name}]: {self.conversation}")
        else:
            print(f"{self.name} doesn't want to talk to you.")

    # fight a character: returns true if the player is still alive after the fight
    def fight(self, weapon, player):  # pylint: disable=unused-argument

        # print a message that the character doesn't want to fight (because normal characters don't fight)
        print(f"{self.name} does not want to fight you.")

    def hug(self):
        if self.hug_message:
            print(self.hug_message)
        else:
            print("I doubt they'd appreciate that.")

    def get_conversation(self):
        return self.conversation

    def set_conversation(self, new_conversation):
        self.conversation = new_conversation

    def set_hug_message(self, new_hug_message):
        self.hug_message = new_hug_message


class Stranger(Character):

    # define constructor and add a "deadly" attribute defining whether the stranger kills a player when fought
    def __init__(self, art, class_name, deadly):
        super().__init__(art, class_name)
        self.deadly = deadly

    # print a line describing the stranger
    def describe(self):
        print(f"You see {self.art_name}, {self.description}")

    # talk to the stranger
    def talk(self):

        # if a conversation is set print it along with the strangers class name
        # if none is set print a message that the stranger doesn't want to talk to you
        if self.conversation:
            print(f"[{self.c_the_name}]: {self.conversation}")
        else:
            print(f"{self.c_the_name} doesn't want to talk to you.")

    # fight a stranger: returns true if the player is still alive after a fight
    def fight(self, weapon, player):

        # if the stranger is deadly the player dies and receives a message that the stranger didn't wish them harm
        if self.deadly:
            print(f"{self.c_the_name} didn't wish you harm. But you already started the fight. You lose ...\nYou die ...")
            player.die()

        # if the stranger is not deadly the player kills the stranger and receives a message about it
        else:
            print(f"You kill {self.c_the_name}.\nThis wasn't right ... You feel sorry for {self.c_the_name}.")
            player.get_current_room().remove_character(self)


class Friend(Character):

    # call the constructor of the super class
    def __init__(self, character_name):
        super().__init__("", character_name)

    # hug the friend: prints a friendly message
    def hug(self):
        if self.hug_message:
            print(self.hug_message)
        else:
            print(f"{self.name} hugs you back.")

    # fight the friend: the game doesn't let you and displays a message about it
    def fight(self, weapon, player):
        print("You wouldn't want to hurt a friend, would you?")


class Enemy(Character):

    # define constructor and add a "weaknesses" list to hold the items a enemy is fightable with
    def __init__(self, art, character_name):
        super().__init__(art, character_name)
        self.weaknesses = []
        self.kill_message = None

    # fight the enemy: returns true if the player is still alive after the fight
    def fight(self, weapon, player):

        # if the used weapon is in the weaknesses list do the following
        if weapon in self.weaknesses and weapon.req_are_met(player):

            # print a message that the enemy was killed
            weapon.print_kill_message(self)

            # remove the enemy from the current room
            player.get_current_room().remove_character(self)

            # add a kill to the killcounter
            player.add_kill()

        elif not weapon.req_are_met(player):
            weapon.print_no_req_message()
            player.die()
        # if it is not
        else:
            # print a message that the player has died
            self.print_kill_message()
            player.die()

    def hug(self):
        if self.hug_message:
            print(self.hug_message)
        else:
            print("You wouldn't want to hug this malicious creature.")

    # getters and setters
    def get_weakness(self):
        return self.weaknesses

    def add_weakness(self, new_weakness):
        self.weaknesses.append(new_weakness)

    def remove_weakness(self, weakness):
        self.weaknesses.remove(weakness)

    def set_kill_message(self, message):
        self.kill_message = message

    def print_kill_message(self):
        if self.kill_message:
            print(self.kill_message)
        else:
            print(f"{self.c_the_name} lands a fatal blow. You die ...")


class Miniboss(Enemy):
    def __init__(self, character_name):
        super().__init__("", character_name)


class Endboss(Enemy):

    # define constructor
    # and add a title
    # and add a "kills_needed" attribute, defining how many kills the player must have to kill the boss
    def __init__(self, character_name, title):
        super().__init__("", character_name)
        self.title = title
        self.the_title = f"the {self.title}"
        self.c_the_title = f"The {self.title}"
        self.add_alias(self.title)
        self.add_alias(self.the_title)
        self.add_alias(f"{self.name} {self.title}")
        self.add_alias(f"{self.name} {self.the_title}")

    # print a line describing the boss
    def describe(self):
        print(f"You see {self.name}, the {self.title}, {self.description}")

    # fight the boss: returns true if the player is still alive after the fight
    def fight(self, weapon, player):
        super().fight(weapon, player)
        if player.isalive():
            player.win()


class Mob(Enemy):

    # print a line describing the mob
    def describe(self):
        print(f"You see {self.art_name}, looking malevolently at you.")

    # talk to the mob: they always say the same thing
    def talk(self):
        print(f"[The {self.name}]: *unintelligible bestial sounds*")
