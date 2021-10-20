class Character:
    def __init__(self, character_name):
        self.name = character_name
        self.description = None
        self.conversation = None

    def describe(self):
        print(f"You see {self.name}, {self.description}.")

    def talk(self):
        if self.conversation:
            print(f"[{self.name}]: {self.conversation}")
        else:
            print(f"{self.name} doesn't want to talk to you.")

    def fight(self, weapon, player):
        print(f"{self.name} does not want to fight you.")
        return True

    def get_name(self):
        return self.name

    def get_desc(self):
        return self.description

    def set_desc(self, new_description):
        self.description = new_description

    def get_conversation(self):
        return self.conversation

    def set_conversation(self, new_conversation):
        self.conversation = new_conversation


class Stranger(Character):
    def __init__(self, class_name):
        super().__init__(class_name)

    def describe(self):
        print(f"You see a {self.name}, {self.description}")

    def talk(self):
        if self.conversation:
            print(f"[The {self.name}]: {self.conversation}")
        else:
            print(f"{self.name} doesn't want to talk to you.")


class Friend(Character):
    def __init__(self, character_name):
        super().__init__(character_name)

    def hug(self):
        print(f"{self.name} hugs you back.")


class Enemy(Character):
    def __init__(self, character_name):
        super().__init__(character_name)
        self.weaknesses = []

    def fight(self, weapon, player):
        if weapon in self.weaknesses:
            print(f"You kill {self.name} with the {weapon.get_name()}!")
            player.get_current_room().remove_character(self)
            return True
        else:
            print(f"{self.name} lands a fatal blow. You die ...")
            return False

    def get_weakness(self):
        return self.weaknesses

    def add_weakness(self, new_weakness):
        self.weaknesses.append(new_weakness)

    def remove_weakness(self, weakness):
        self.weaknesses.remove(weakness)


class Mob(Enemy):
    def __init__(self, class_name):
        super().__init__(class_name)

    def fight(self, weapon, player):
        if weapon in self.weaknesses:
            print(f"You kill the {self.name} with the {weapon.get_name()}!")
            player.get_current_room().remove_character(self)
            return True

        else:
            print(f"The {self.name} lands a fatal blow. You die ...")
