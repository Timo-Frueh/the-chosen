class Commands:
    
    commands = {"north": "move north",
                "east": "move east",
                "south": "move south",
                "west": "move west",
                "look": "look at your surroundings",
                "talk": "talk to someone in the room",
                "inventory": "\bshow what you are carrying",
                "quit": "quit the game -> NOTE: you will not be able to restore the game later",
                "help": "show this list"}
    
    @classmethod
    def print_commands(cls):
        for command in cls.commands:
            print(f"{command}:\t\t{cls.commands[command]}")

    @staticmethod
    def movement(player, direction):
        player.move(direction)
        player.get_current_room().describe()

    @staticmethod
    def look(player):
        player.get_current_room().describe()

    @staticmethod
    def talk(player):
        if player.get_current_room().get_characters():
            talk_to = input("Talk to whom? ").lower().replace(" ", "")

            if player.get_current_room().get_character(talk_to):
                player.get_current_room().get_character(talk_to).talk()

            else:
                print(f"There is no {talk_to} here.")

        else:
            print("There is no one here to listen to your beautiful voice.")

    @staticmethod
    def show_inventory(player):
        if player.get_inventory():
            print("You are carrying:")
            for item in player.get_inventory():
                print(item)
        else:
            print("You are empty-handed.")

    @staticmethod
    def fight(player):
        pass

    @staticmethod
    def quit():
        confirm = input("Do you really whish to leave the game? [y|n] ")
        return confirm
