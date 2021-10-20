class Item:
    def __init__(self, item_name):
        self.name = item_name
        self.name_w_art = f"a {item_name}"
        self.description = None

    def describe(self):
        print(f"{self.name_w_art.capitalize()} is here, {self.description}.")

    def get_name(self, art):
        if art:
            return self.name_w_art
        else:
            return self.name

    def get_description(self):
        return self.description

    def set_description(self, new_description):
        self.description = new_description


class Artifact(Item):
    def __init__(self, item_name, initial_room):
        super().__init__(item_name)
        self.name_w_art = f"the {item_name}"
        self.initial_room = initial_room
        self.initial_description = None

    def describe_initial(self):
        print(f"{self.name_w_art} is here, {self.initial_description}.")

    def get_initial_description(self):
        return self.initial_description

    def set_initial_description(self, initial_description):
        self.initial_description = initial_description

    def get_initial_room(self):
        return self.initial_room

    def set_initial_room(self, initial_room):
        self.initial_room = initial_room


class Artifacts(Artifact):
    def __init__(self, item_name, initial_room):
        super().__init__(item_name, initial_room)

    def describe(self):
        print(f"{self.name_w_art.capitalize()} are here, {self.description}.")

    def describe_initial(self):
        print(f"{self.name_w_art.capitalize()} are here, {self.initial_description}.")
