class Commands:

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
