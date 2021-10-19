class Commands:

    @staticmethod
    def movement(player, direction):
        player.move(direction)
        player.get_current_room().describe()

    @staticmethod
    def look(player):
        player.get_current_room().describe()

    @staticmethod
    def quit():
        confirm = input("Do you really want to quit? [y|n] ")
        return confirm
