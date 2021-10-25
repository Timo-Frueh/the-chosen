class InputInterpreter:

    @staticmethod
    def interpret_single(command, key):
        output = command.replace(key, "")

        return output.strip()

    @staticmethod
    def interpret_double(command, key, separator):
        without_key = command.replace(key, "")
        output = without_key.split(separator)

        try:
            output[1]
        except IndexError:
            output.append("")

        return [output[0].strip(), output[1].strip()]
