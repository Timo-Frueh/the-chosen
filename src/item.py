class Item:
    def __init__(self, art, item_name):
        self.name = item_name
        self.art = art
        self.name_w_art = f"{self.art} {self.name}"
        self.name_w_cap_art = f"{self.art.capitalize()} {self.name}"
        self.description = None

    def describe(self):
        print(f"{self.name_w_cap_art} is here, {self.description}.")

    def get_name(self):
        return self.name

    def get_name_w_art(self):
        return self.name_w_art

    def get_name_w_cap_art(self):
        return self.name_w_cap_art

    def get_description(self):
        return self.description

    def set_description(self, new_description):
        self.description = new_description


class Artifact(Item):
    def __init__(self, art, item_name, initial_room):
        super().__init__(art, item_name)
        self.art = "the"
        self.initial_room = initial_room
        self.initial_description = None

    def describe_initial(self):
        print(f"{self.name_w_cap_art} is here, {self.initial_description}.")

    def get_initial_description(self):
        return self.initial_description

    def set_initial_description(self, initial_description):
        self.initial_description = initial_description

    def get_initial_room(self):
        return self.initial_room


class Artifacts(Artifact):
    def __init__(self, art, item_name, initial_room):
        super().__init__(art, item_name, initial_room)
        self.art = art

    def describe(self):
        print(f"{self.name_w_cap_art} are here, {self.description}.")

    def describe_initial(self):
        print(f"{self.name_w_cap_art} are here, {self.initial_description}.")
