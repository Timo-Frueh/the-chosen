class Commands:
    
    commands = {"north": "move north",
                "east": "move east",
                "south": "move south",
                "west": "move west",
                "look": "look at your surroundings",
                "talk": "talk to someone in the room",
                "quit": "quit the game -> NOTE: you will not be able to restore the game later",
                "help": "show this list"}
    
    @classmethod
    def print_commands(cls):
        for command in cls.commands:
            print(f"{command}:\t {cls.commands[command]}")

    @staticmethod
    def movement(player, direction):
        player.move(direction)
        player.get_current_room().describe()

    @staticmethod
    def look(player):
        player.get_current_room().describe()

    @staticmethod
    def talk(player):
        talk_to = input("Talk to whom? ").lower().replace(" ", "")
        for character in player.get_current_room().get_characters():
            if character.get_name().lower().replace(" ", "") == talk_to:
                character.talk()

    @staticmethod
    def quit():
        confirm = input("Do you really want to quit? [y|n] ")
        return confirm
