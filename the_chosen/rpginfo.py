# coding=utf-8

"""
This module holds the RPGInfo class.
"""

# The Chosen  Copyright (C) 2021  Timo Früh
# Full copyright notice in main.py

import the_chosen.io as io


class RPGInfo:

    # define some class variables
    author = None
    title = None
    subtitle = None
    welcome_message = None

    @classmethod
    def welcome(cls):
        """
        Print a welcome message.
        """

        io.ch_print(f"Welcome to {cls.title}: {cls.subtitle}")
        io.ch_print("")
        io.ch_print(cls.welcome_message)

    @classmethod
    def credits(cls):
        """
        Print credits.
        """

        io.ch_print(f"This was {cls.title}.")
        io.ch_print("Thank you for playing!")
        io.ch_print(f"\nMade by {cls.author}.")
