# coding=utf-8

"""
This module holds the ResourceHelper class.
"""

# The Chosen  Copyright (C) 2021  Timo Früh
# Full copyright notice in main.py

import os


class ResourceHelper:
    """
    This class contains three class methods to help with reading text resources.
    """

    resources_path = ""

    @classmethod
    def set_resources_path(cls, path):
        """
        Set the resources path.

        :param path: The resources path.
        :type path: str
        """

        cls.resources_path = path

    @classmethod
    def read_resource(cls, resource):
        """
        Read a text resource in the resource folder.

        :param resource: The resource to be read.
        :type resource: str

        :return: The content of the file as text.
        :rtype: str
        """
        with open(os.path.join(cls.resources_path, resource), "r", encoding="UTF-8") as file:
            return file.read()

    @classmethod
    def read_split_resource(cls, resource, split="\n---\n"):
        """
        Read a text resource which has to be split first.

        :param resource: The resource to be read.
        :type resource: str

        :param split: Where the resource should be split.
        :type split: str

        :return: The split resource.
        :rtype: list
        """

        with open(os.path.join(cls.resources_path, resource), "r", encoding="UTF-8") as file:
            return file.read().split(split)
