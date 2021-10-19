from rpginfo import RPGInfo
from room import Room
from player import Player
from character import Character, Friend, Enemy
from commands import Commands as Cmd
from item import Item

import os
from clear_screen import clear


class Main:
    def __init__(self):

        clear()

        self.file_path = os.path.dirname(os.path.abspath(__file__))
        self.welcome_file = open(os.path.join(self.file_path, "resources", "welcome_message.txt"), "r")
        self.cellar_desc_file = open(os.path.join(self.file_path, "resources", "cellar_description.txt"), "r")

        RPGInfo.author = "Timo Früh"
        RPGInfo.title = "The Chosen"
        RPGInfo.subtitle = "At Nights End"

        RPGInfo.welcome_message = self.welcome_file.read()

        RPGInfo.welcome()

        self.cellar = Room(room_name="Cellar")
        self.cellar.set_desc(self.cellar_desc_file.read())

        self.stairwell = Room(room_name="Stairwell to the Cellar")
        self.stairwell.set_desc("Stairwell description")

        self.hall = Room(room_name="The Hall")
        self.hall.set_desc("Hall description")

        self.west_room = Room(room_name="Room West to the Hall")
        self.west_room.set_desc("West Room description")

        self.trophy_room = Room(room_name="Trophy Room")
        self.trophy_room.set_desc("Trophy Room description")

        self.ns_passageway = Room(room_name="N/S Passageway")
        self.ns_passageway.set_desc("N/S Passageway description")

        self.staff_room = Room(room_name="Library Staff Room")
        self.staff_room.set_desc("Staff Room description")

        self.library = Room(room_name="The Library")
        self.library.set_desc("Library description")

        self.library_entrance = Room(room_name="Library Entrance")
        self.library_entrance.set_desc("Library Entrance description")

        self.east_room = Room(room_name="Room East to the Hall")
        self.east_room.set_desc("East Room description")

        self.throne_entrance = Room(room_name="Entrance to the Throne Room")
        self.throne_entrance.set_desc("Throne Room Entrance description")

        self.hidden_room = Room(room_name="Hidden Room")
        self.hidden_room.set_desc("Hidden Room description")

        self.throne_room = Room(room_name="The Throne Room")
        self.throne_room.set_desc("Throne Room description")

        self.cellar.link_room(direction="west", room=self.stairwell)
        self.stairwell.link_room(direction="east", room=self.cellar)

        self.stairwell.link_room(direction="north", room=self.hall)
        self.hall.link_room(direction="south", room=self.stairwell)

        self.hall.link_room(direction="west", room=self.west_room)
        self.west_room.link_room(direction="east", room=self.hall)

        self.west_room.link_room(direction="west", room=self.trophy_room)
        self.trophy_room.link_room(direction="east", room=self.west_room)

        self.trophy_room.link_room(direction="north", room=self.ns_passageway)
        self.ns_passageway.link_room(direction="south", room=self.trophy_room)

        self.ns_passageway.link_room(direction="north", room=self.staff_room)
        self.staff_room.link_room(direction="south", room=self.ns_passageway)

        self.staff_room.link_room(direction="east", room=self.library)
        self.library.link_room(direction="west", room=self.staff_room)

        self.library.link_room(direction="south", room=self.library_entrance)
        self.library_entrance.link_room(direction="north", room=self.library)

        self.library_entrance.link_room(direction="south", room=self.hall)
        self.hall.link_room(direction="north", room=self.library_entrance)

        self.hall.link_room(direction="east", room=self.throne_entrance)
        self.throne_entrance.link_room(direction="west", room=self.hall)

        self.throne_entrance.link_room(direction="north", room=self.throne_room)
        self.throne_room.link_room(direction="south", room=self.throne_entrance)

        self.player_name = input("What is your name? ")
        if self.player_name.replace(" ", "") == "":
            self.player_name = "Stranger"
        self.player = Player(player_name=self.player_name, starting_room=self.cellar)

        self.longsword = Item(item_name="sword")
        self.longsword.set_description("a typical European longsword of a length a bit longer than your arm")
        self.cellar.add_item(self.longsword)

        print("\nYou look around.")

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
