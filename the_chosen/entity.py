# coding=utf-8

"""
This module holds the entity class.
"""

# The Chosen  Copyright (C) 2021-2023  Timo Früh
# Full copyright notice in __main__.py


class Entity:
    """
    This class is the base class for all Items and Characters. Its main use is the handling of names.
    """

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

        self.aliases = [self.name.lower().strip(), self.art_name.lower().strip(), self.the_name.lower().strip()]

        self.description = None

    # getters and setters
    def get_description(self):
        """
        Return the entity's description.

        :return: The entity's description.
        :rtype: str
        """

        return self.description

    def get_name(self):
        """
        Return the entity's name.

        :return: The entity's name.
        :rtype: str
        """

        return self.name

    def set_description(self, new_description):
        """
        Set the entity's description.

        :param new_description: The new description to be set.
        :type new_description: str
        """

        self.description = new_description

    def get_aliases(self):
        """
        Return the entity's aliases (the names it can be referred to by).

        :return: The entity's aliases list.
        :rtype: list
        """

        return self.aliases
    
    def add_alias(self, new_alias):
        """
        Add a new alias to the entity's aliases list.

        :param new_alias: The new alias to be added.
        :type new_alias: str
        """

        self.aliases.append(new_alias.lower().strip())

    def get_art_name(self):
        """
        Return the entity's name with the correct article (if it has an article).

        :return: The entity's name with the correct article.
        :rtype: str
        """

        return self.art_name
    
    def get_c_art_name(self):
        """
        Return the entity's name with the correct capitalized article (if it has an article).

        :return: The entity's name with the correct capitalized article.
        :rtype: str
        """

        return self.c_art_name
    
    def get_the_name(self):
        """
        Return the entity's name with "the" (if it has an article).

        :return: The entity's name with "the".
        :rtype: str
        """

        return self.the_name
    
    def get_c_the_name(self):
        """
        Return the entity's name with "The" (if it has an article).

        :return: The entity's name with "The".
        :rtype: str
        """

        return self.the_name
