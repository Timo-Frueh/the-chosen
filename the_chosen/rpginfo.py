# coding=utf-8

# The Chosen  Copyright (C) 2021  Timo Früh
# Full copyright notice in main.py

class RPGInfo:

    # define the class variables
    author = None
    title = None
    subtitle = None
    welcome_message = None

    # print a welcome message
    @classmethod
    def welcome(cls):
        print(f"Welcome to {cls.title}: {cls.subtitle}")
        print("")
        print(cls.welcome_message)

    # print credits
    @classmethod
    def credits(cls):
        print(f"This was {cls.title}.")
        print("Thank you for playing!")
        print(f"\nMade by {cls.author}.")
