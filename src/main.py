from rpginfo import RPGInfo
from room import Room
from character import Character, Friend, Enemy
from player import Player
from commands import Commands as Cmd
from item import Item

from clear_screen import clear


class Main:
    def __init__(self):

        clear()

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

        self.player_name = input("Who are you? ")
        if self.player_name.replace(" ", "") == "":
            self.player_name = "Stranger"
        self.player = Player(player_name=self.player_name, starting_room=self.testroom)

        self.sword = Item("sword")
        self.sword.set_description("a normal longsword about the length of your arm.")
        self.player.add_to_inventory(self.sword)

        self.elliot = Friend(character_name="Elliot")
        self.elliot.set_desc("a man you've never seen before. Or have you? How else would you know his name?")
        self.elliot.set_conversation(f"Hey, {self.player.get_name()}! Long time no see!")
        self.testroom.add_character(self.elliot)

        self.derek = Enemy(character_name="Derek")
        self.derek.set_desc("a nasty smelling werewolf.")
        self.derek.add_weakness(self.sword)
        self.testroom2.add_character(self.derek)

        print("")

        self.player.get_current_room().describe()

    def mainloop(self):

        alive = True
        victory = False

        while alive and not victory:
            print("")
            command = input("> ").lower().replace(" ", "")

            if command in ["commands", "help", "?"]:
                Cmd.print_commands()

            elif command in ["north", "east", "south", "west"]:
                Cmd.movement(self.player, command)

            elif command in ["look", "l"]:
                Cmd.look(self.player)

            elif command == "talk":
                Cmd.talk(self.player)

            elif command in ["inventory", "i", "backpack"]:
                Cmd.show_inventory(self.player)

            elif command == "fight":
                alive = Cmd.fight(self.player)

            elif command == "take":
                Cmd.take(self.player)

            elif command == "drop":
                Cmd.drop(self.player)

            elif command in ["quit", "exit"]:
                confirm = Cmd.quit()
                if confirm == "y":
                    alive = False

            else:
                print(f"I do not know what you meant by {command}.")

        print("")
        RPGInfo.credits()
        print("")

        input("[Hit any key to exit.]")
        clear()


if __name__ == "__main__":
    Game = Main()

    Game.mainloop()
