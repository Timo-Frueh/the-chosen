from rpginfo import RPGInfo
from room import Room
from character import Character
from player import Player


class Main:
    def __init__(self):

        RPGInfo.author = "Timo Früh"
        RPGInfo.title = "Title"
        RPGInfo.subtitle = "Subtitle"
        RPGInfo.welcome_message = "Welcome message"

        RPGInfo.welcome()

        print("")

        self.testroom = Room(room_name="Testroom")
        self.testroom.set_desc("This is a testroom")

        self.testroom2 = Room(room_name="Testroom 2")
        self.testroom2.set_desc("This is another testroom")

        self.testroom.link_room("south", self.testroom2)
        self.testroom2.link_room("north", self.testroom)

        self.elliot = Character(character_name="Elliot")
        self.elliot.set_desc("a man you've never seen before. Or have you? How else would you know his name?")
        self.testroom2.add_character(self.elliot)

        self.player_name = input("Who are you? ")
        self.player = Player(player_name=self.player_name, starting_room=self.testroom)

        print("")

        self.player.get_current_room().describe()

    def mainloop(self):

        dead = False
        victory = False

        while not dead or victory:
            print("")
            command = input("> ").lower().replace(" ", "")

            if command in ["north", "east", "south", "west"]:
                self.player.move(command)
                self.player.get_current_room().describe()

            elif command in ["quit", "exit"]:
                confirm = input("Do you really want to quit? [y|n] ")
                if confirm == "y":
                    dead = True

            elif command in ["look", "l"]:
                self.player.get_current_room().describe()

            else:
                print(f"I do not know what you mean by {command}.")

        print("")

        RPGInfo.credits()


if __name__ == "__main__":
    Game = Main()

    Game.mainloop()
