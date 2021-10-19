class Commands:
    
    commands = {"north     ": "  move north",
                "east      ": "  move east",
                "south     ": "  move south",
                "west      ": "  move west",
                "look      ": "  look at your surroundings",
                "talk      ": "  talk to someone in the room",
                "inventory ": "  show what you are carrying",
                "fight     ": "  fight someone",
                "take      ": "  put something into your inventory",
                "drop      ": "  drop something in your inventory",
                "quit      ": "  quit the game -> NOTE: you will not be able to restore the game later",
                "help      ": "  show this list"}
    
    @classmethod
    def print_commands(cls):
        for command in cls.commands:
            print(f"{command}:{cls.commands[command]}")

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
                    print(f"You do not have a {fight_with}.")

            else:
                print(f"There is no {enemy.get_name()} here.")

        else:
            print("There is no one here to fight.")

        return alive

    @staticmethod
    def take(player):
        if player.get_current_room().get_items():
            take = input("What do you want to take? ").lower().replace(" ", "")
            item = player.get_current_room().get_item(take)

            if item:
                player.get_current_room().remove_item(item)
                player.add_to_inventory(item)
                print("Taken.")
            else:
                print(f"There is no {take} here.")

        else:
            print("There is nothing here to take.")

    @staticmethod
    def drop(player):
        if player.get_inventory():
            drop = input("What do you want do drop? ")
            item = player.get_inventory_item(drop)

            if item:
                player.remove_from_inventory(item)
                player.get_current_room().add_item(item)
                print("Dropped.")
            else:
                print(f"You do not have a {drop}.")

        else:
            print("You do not have anything to drop.")

    @staticmethod
    def quit():
        confirm = input("Do you really whish to leave the game? [y|n] ")
        return confirm
