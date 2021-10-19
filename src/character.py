class Character:
    def __init__(self, character_name):
        self.name = character_name
        self.description = None
        self.conversation = None

    def describe(self):
        print(f"You see {self.name}, {self.description}")

    def talk(self):
        print(f"[{self.name}]: {self.conversation}")

    def fight(self):
        print(f"{self.name} does not want to fight you")

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
