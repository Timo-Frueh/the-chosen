# coding=utf-8

"""
This module holds the RPGInfo class.
"""

# The Chosen  Copyright (C) 2021  Timo Früh
# Full copyright notice in main.py


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

        print(f"Welcome to {cls.title}: {cls.subtitle}")
        print("")
        print(cls.welcome_message)

    @classmethod
    def credits(cls):
        """
        Print credits.
        """
        
        print(f"This was {cls.title}.")
        print("Thank you for playing!")
        print(f"\nMade by {cls.author}.")
