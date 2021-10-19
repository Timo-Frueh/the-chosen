class Commands:
    
    commands = {"north": "move north",
                "east": "move east",
                "south": "move south",
                "west": "move west",
                "look": "look at your surroundings",
                "talk": "talk to someone in the room",
                "inventory": "\bshow what you are carrying",
                "fight": "fight someone",
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
            character = player.get_current_room().get_character(talk_to)

            if character:
                character.talk()

            else:
                print(f"There is no {talk_to} here.")

        else:
            print("There is no one here to listen to your beautiful voice.")

    @staticmethod
    def show_inventory(player):
        if player.get_inventory():
            print("You are carrying:")
            for item in player.get_inventory():
                print(f"- A {item.get_name()}")
        else:
            print("You are empty-handed.")

    @staticmethod
    def fight(player):
        alive = True

        if player.get_current_room().get_characters():
            fight = input("Fight whom? ").lower().replace(" ", "")
            enemy = player.get_current_room().get_character(fight)

            if enemy:
                fight_with = input("What do you want to fight with? ").lower().replace(" ", "")
                weapon = player.get_inventory_item(fight_with)

                if weapon:
                    alive = player.get_current_room().get_character(fight).fight(weapon)
                else:
                    print(f"You do not have a {weapon}.")

            else:
                print("There is no one here to fight.")

        return alive

    @staticmethod
    def quit():
        confirm = input("Do you really whish to leave the game? [y|n] ")
        return confirm
