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
    def get_resource(cls, resource):
        return open(os.path.join(cls.resources_path, resource), "r")

