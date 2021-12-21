# coding=utf-8

# The Chosen  Copyright (C) 2021  Timo Früh
# Full copyright notice in main.py

class Entity:
    def __init__(self, art, name):
        self.name = name
        self.art = art

        if art.strip() == "":
            self.art_name = self.name
            self.c_art_name = self.name
            self.the_name = self.name
            self.c_the_name = self.name
        else:
            self.art_name = f"{self.art} {self.name}"
            self.c_art_name = f"{self.art.capitalize()} {self.name}"
            self.the_name = f"the {self.name}"
            self.c_the_name = f"The {self.name}"

        self.aliases = [self.name.lower().strip(), self.art_name, self.the_name]

        self.description = None

    def get_description(self):
        return self.description

    def get_name(self):
        return self.name

    def set_description(self, new_description):
        self.description = new_description

    def get_aliases(self):
        return self.aliases
    
    def add_alias(self, new_alias):
        self.aliases.append(new_alias.lower().strip())

    def get_art_name(self):
        return self.art_name
    
    def get_c_art_name(self):
        return self.c_art_name
    
    def get_the_name(self):
        return self.the_name
    
    def get_c_the_name(self):
        return self.the_name
