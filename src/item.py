class Item:
    def __init__(self, item_name):
        self.name = item_name
        self.description = None

    def describe(self):
        print(f"There is a {self.name} here.")

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def set_description(self, new_description):
        self.description = new_description
