# coding=utf-8

# The Chosen  Copyright (C) 2021  Timo Früh
# Full copyright notice in main.py

class InputInterpreter:

    # define a static method to interpret a positional command with a single argument
    @staticmethod
    def interpret_single(command, key, remove):

        # replace the command with nothing so that only the argument remains
        output = command.replace(key, "")

        for w in remove:
            output = output.replace(w, "")

        # return the argument, stripped from whitespaces at end and beginning
        return output.strip()

    # define a static method to interpret a positional command with two arguments
    @staticmethod
    def interpret_double(command, key, separator, remove):

        # replace the command with nothing so that only the arguments and the separator remain
        without_key = command.replace(key, "")

        for w in remove:
            output = without_key.replace(w, "")

        # split the above at the separator and thereby removing the separator
        output = without_key.split(separator)

        # try to access the second argument
        try:
            output[1]

        # if there was none add a second empty argument
        except IndexError:
            output.append("")

        # return the arguments in a list and stripped of whitespaces at end and beginning
        return [output[0].strip(), output[1].strip()]
