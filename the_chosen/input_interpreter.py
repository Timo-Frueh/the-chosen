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

    @staticmethod
    def interpret_single(command: str, key: str, remove: list = None):

        """
        Intepret a command with only one argument.

        :param command: the whole command the user has typed
        :type command: str

        :param key: command key that should trigger this command, e.g. "fight"
        :type key: str

        :param remove: a list of words (strings) to remove from the users input
        :type remove: list
        """

        # replace the command with nothing so that only the argument remains
        output = command.replace(key, "")

        if remove:
            for word in remove:
                output = output.replace(word, " ")

        # return the argument, stripped from whitespaces at end and beginning
        return output.lower().strip()

    # define a static method to interpret a positional command with two arguments
    @staticmethod
    def interpret_double(command: str, key:str, separator:str, remove_0: list = None, remove_1:list = None):

        """
        Interpret a command with two arguments.

        :param command: the whole command the user has typed
        :type command: str

        :param key: command key that should trigger this command, e.g. "fight"
        :type key: str

        :param separator: command separator that is between the two arguments, e.g. "with"
        :type separator: str

        :param remove_0: list of words (strings) to remove from the first argument
        :type remove_0: list

        :param remove_1: list of words (strings) to remove from the second argument
        :type remove_1: list
        """

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
