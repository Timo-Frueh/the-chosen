"""
This file holds the InputInterpreter class.
"""
# coding=utf-8

# The Chosen  Copyright (C) 2021  Timo Früh
# Full copyright notice in main.py

class InputInterpreter:
    """
    This class is used to interpret the commands typed by the user.
    """

    # define a static method to interpret a positional command with a single argument
    @staticmethod
    def interpret_single(command, key, remove: list = None):

        # replace the command with nothing so that only the argument remains
        output = command.replace(key, "")

        if remove:
            for w in remove:
                output = output.replace(w, " ")

        # return the argument, stripped from whitespaces at end and beginning
        return output.lower().strip()

    # define a static method to interpret a positional command with two arguments
    @staticmethod
    def interpret_double(command, key, separator, remove_0: list = None, remove_1:list = None):

        # replace the command with nothing so that only the arguments and the separator remain
        without_key = command.replace(key, "")

        # split the above at the separator and thereby removing the separator
        output = without_key.split(separator)

        # try to access the second argument
        try:
            output[1]

        # if there was none add a second empty argument
        except IndexError:
            output.append("")

        if remove_0:
            for word in remove_0:
                output[0] = output[0].replace(word, " ")

        if remove_1:
            for word in remove_1:
                output[1] = output[1].replace(word, " ")

        # return the arguments in a list and stripped of whitespaces at end and beginning
        return [output[0].lower().strip(), output[1].lower().strip()]
