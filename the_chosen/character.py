# coding=utf-8

# The Chosen  Copyright (C) 2021  Timo Früh
# Full copyright notice in main.py

class Character:

    # define constructor and the three opject attributes
    def __init__(self, character_name):
        self.name = character_name
        self.aliases = [character_name.lower().strip()]
        self.description = None
        self.conversation = None

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
    def fight(self, weapon, player):

        # print a message that the character doesn't want to fight (because normal characters don't fight)
        print(f"{self.name} does not want to fight you.")
        return True

    # getters and setters
    def get_name(self):
        return self.name

    def get_aliases(self):
        return self.aliases

    def add_alias(self, alias):
        self.aliases.append(alias.lower().strip())

    def get_desc(self):
        return self.description

    def set_desc(self, new_description):
        self.description = new_description

    def get_conversation(self):
        return self.conversation

    def set_conversation(self, new_conversation):
        self.conversation = new_conversation

    # this get_title() method doesn't do anything but is needed later for bosses
    def get_title(self):
        return ""


class Stranger(Character):

    # define constructor and add a "deadly" attribute defining whether the stranger kills a player when fought
    def __init__(self, class_name, deadly):
        super().__init__(class_name)
        self.deadly = deadly

    # print a line describing the stranger
    def describe(self):
        print(f"You see a {self.name}, {self.description}")

    # talk to the stranger
    def talk(self):

        # if a conversation is set print it along with the strangers class name
        # if none is set print a message that the stranger doesn't want to talk to you
        if self.conversation:
            print(f"[The {self.name}]: {self.conversation}")
        else:
            print(f"The {self.name} doesn't want to talk to you.")

    # fight a stranger: returns true if the player is still alive after a fight
    def fight(self, weapon, player):

        # if the stranger is deadly the player dies and receives a message that the stranger didn't wish them harm
        if self.deadly:
            print(f"The {self.name} didn't wish you harm. But you already started the fight. You lose ...\nYou die ...")
            return False

        # if the stranger is not deadly the player kills the stranger and receives a message about it
        else:
            print(f"You kill the {self.name}.\nThis wasn't right ... You feel sorry for the {self.name}.")
            player.get_current_room().remove_character(self)
            return True


class Friend(Character):

    # call the constructor of the super class
    def __init__(self, character_name):
        super().__init__(character_name)

    # hug the friend: prints a friendly message
    def hug(self):
        print(f"{self.name} hugs you back.")

    # fight the friend: the game doesn't let you and displays a message about it
    def fight(self, weapon, player):
        print("You wouldn't want to hurt a friend, would you?")
        return True


class Enemy(Character):

    # define constructor and add a "weaknesses" list to hold the items a enemy is fightable with
    def __init__(self, character_name):
        super().__init__(character_name)
        self.weaknesses = []

    # fight the enemy: returns true if the player is still alive after the fight
    def fight(self, weapon, player):

        # if the used weapon is in the weaknesses list do the following
        if weapon in self.weaknesses:

            # print a message that the enemy was killed
            print(f"You kill {self.name} with the {weapon.get_name()}!")

            # remove the enemy from the current room
            player.get_current_room().remove_character(self)

            # add a kill to the killcounter
            player.add_kill()
            return True

        # if it is not
        else:

            # print a message that the player has died
            print(f"{self.name} lands a fatal blow.\nYou die ...")
            return False

    # getters and setters
    def get_weakness(self):
        return self.weaknesses

    def add_weakness(self, new_weakness):
        self.weaknesses.append(new_weakness)

    def remove_weakness(self, weakness):
        self.weaknesses.remove(weakness)


class Boss(Enemy):

    # define constructor
    # and add a title
    # and add a "kills_needed" attribute, defining how many kills the player must have to kill the boss
    def __init__(self, character_name, title, kills_needed):
        super().__init__(character_name)
        self.kills_needed = kills_needed
        self.title = title

    # print a line describing the boss
    def describe(self):
        print(f"You see {self.name}, the {self.title}, {self.description}")

    # fight the boss: returns true if the player is still alive after the fight
    def fight(self, weapon, player):

        # if the used weapon is in the weaknesses list and the player has enough kills do the following
        if weapon in self.weaknesses and player.get_kills() >= self.kills_needed:

            # print a message that the player has killed the boss
            print(f"You kill {self.name} with the {weapon.get_name()}!")

            # remove the boss from the current room
            player.get_current_room().remove_character(self)

            # add a kill to the killcounter
            player.add_kill()
            return True

        # if it is not or the kills are not enough
        else:

            # display a message that the player has died
            print(f"{self.name} lands a fatal blow.\nYou die ...")
            return False

    # getters and setters
    def get_title(self):
        return self.title


class Mob(Enemy):

    # call the constructor of the super class
    def __init__(self, class_name):
        super().__init__(class_name)

    # print a line describing the mob
    def describe(self):
        print(f"You see a {self.name}, looking malevolently at you.")

    # fight the mob: return true if the player is still alive after the fight
    def fight(self, weapon, player):

        # if the used weapon is in the weaknesses list do the following
        if weapon in self.weaknesses:

            # print a message that the mob was killed by the player
            print(f"You kill the {self.name} with the {weapon.get_name()}!")

            # remove the mob from the current room
            player.get_current_room().remove_character(self)

            # add a kill to the killcounter
            player.add_kill()
            return True

        # if it was not
        else:

            # print a message that the player has died
            print(f"The {self.name} lands a fatal blow.\nYou die ...")
            return False

    # talk to the mob: they always say the same thing
    def talk(self):
        print(f"[The {self.name}]: Long live the Demon King!")
