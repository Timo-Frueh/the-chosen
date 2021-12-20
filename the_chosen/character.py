# coding=utf-8

# The Chosen  Copyright (C) 2021  Timo Früh
# Full copyright notice in main.py

from the_chosen.entity import Entity


class Character(Entity):

    def __init__(self, art, character_name):
        super().__init__(art, character_name)
        self.conversation = None
        self.hug_message = None

    def describe(self):
        print(f"You see {self.name}, {self.description}")

    def talk(self):

        if self.conversation:
            print(f"[{self.name}]: {self.conversation}")
        else:
            print(f"{self.name} doesn't want to talk to you.")

    def fight(self, weapon, player):  # pylint: disable=unused-argument

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

    def __init__(self, art, class_name, deadly):
        super().__init__(art, class_name)
        self.deadly = deadly

    def describe(self):
        print(f"You see {self.art_name}, {self.description}")

    def talk(self):

        if self.conversation:
            print(f"[{self.c_the_name}]: {self.conversation}")
        else:
            print(f"{self.c_the_name} doesn't want to talk to you.")

    def fight(self, weapon, player):

        if self.deadly:
            print(f"{self.c_the_name} didn't wish you harm. But you already started the fight. You lose ...\nYou die ...")
            player.die()

        else:
            print(f"You kill {self.c_the_name}.\nThis wasn't right ... You feel sorry for {self.c_the_name}.")
            player.get_current_room().remove_character(self)


class Friend(Character):

    def __init__(self, character_name):
        super().__init__("", character_name)

    def hug(self):
        if self.hug_message:
            print(self.hug_message)
        else:
            print(f"{self.name} hugs you back.")

    def fight(self, weapon, player):
        print("You wouldn't want to hurt a friend, would you?")


class Enemy(Character):

    def __init__(self, art, character_name):
        super().__init__(art, character_name)
        self.weaknesses = []
        self.kill_messages = {}

    def fight(self, weapon, player):

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
        if self.hug_message:
            print(self.hug_message)
        else:
            print("You wouldn't want to hug this malicious creature.")

    def get_weakness(self):
        return self.weaknesses

    def add_weakness(self, new_weakness):
        self.weaknesses.append(new_weakness)

    def remove_weakness(self, weakness):
        self.weaknesses.remove(weakness)

    def set_def_kill_message(self, message):
        self.kill_messages["def"] = message

    def set_kill_message(self, item_name, message):
        self.kill_messages[item_name] = message

    def print_kill_message(self, item):
        if item.get_name() in self.kill_messages:
            print(self.kill_messages[item.get_name()])
        elif self.kill_messages["def"]:
            print(self.kill_messages["def"])
        else:
            print(f"{self.c_the_name} lands a fatal blow. You die ...")


class Miniboss(Enemy):
    def __init__(self, character_name):
        super().__init__("", character_name)


class Endboss(Enemy):

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
        print(f"You see {self.name}, the {self.title}, {self.description}")

    def fight(self, weapon, player):
        super().fight(weapon, player)
        if player.isalive():
            player.win()


class Mob(Enemy):

    def describe(self):
        print(f"You see {self.art_name}, looking malevolently at you.")

    def talk(self):
        print(f"[The {self.name}]: *unintelligible bestial sounds*")
