# coding=utf-8

# The Chosen  Copyright (C) 2021  Timo Früh
# Full copyright notice in main.py

import os

class ResourceHelper():

    resources_path = ""

    @classmethod
    def set_resources_path(cls, path):
        cls.resources_path = path

    @classmethod
    def read_resource(cls, resource):
        file = open(os.path.join(cls.resources_path, resource), "r")
        return file.read()

