class InputInterpreter:

    @staticmethod
    def interpret_single(command, key):
        output = command.replace(key, "")

        return output

    @staticmethod
    def interpret_double(command, key, separator):
        without_key = command.replace(key, "")
        output = without_key.split(separator)

        try:
            output[1]
        except IndexError:
            output.append(None)

        return output
