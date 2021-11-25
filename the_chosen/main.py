#     coding=utf-8

#     The Chosen: At Nights End: A short text-adventure
#     Copyright (C) 2021 Timo Früh
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

from the_chosen.rpginfo import RPGInfo
from the_chosen.room import Room
from the_chosen.player import Player
from the_chosen.character import Stranger, Friend, Enemy, Endboss, Mob
from the_chosen.commands import Commands as Cmd
from the_chosen.item import Item, Artifacts
from the_chosen.input_interpreter import InputInterpreter
from the_chosen.link import Door, Ladder, IllusoryWall
from the_chosen.direction_helper import DirectionHelper as Dh

import os
from clear_screen import clear


class Main:
    def __init__(self):

        # clear the screen at the beginning of the game
        clear()

        # load all room description files and the welcome message file
        self.file_path = os.path.dirname(os.path.abspath(__file__))
        self.welcome_f = open(os.path.join(self.file_path, "resources", "welcome_message.txt"), "r")
        self.cellar_f = open(os.path.join(self.file_path, "resources", "cellar.txt"), "r")
        self.cellar_ladder_f = open(os.path.join(self.file_path, "resources", "cellar_ladder.txt"), "r")
        self.hall_f = open(os.path.join(self.file_path, "resources", "hall.txt"), "r")
        self.west_room_f = open(os.path.join(self.file_path, "resources", "west_room.txt"), "r")
        self.trophy_room_f = open(os.path.join(self.file_path, "resources", "trophy_room.txt"), "r")
        self.ns_passageway_f = open(os.path.join(self.file_path, "resources", "ns_passageway.txt"), "r")
        self.staff_room_f = open(os.path.join(self.file_path, "resources", "staff_room.txt"), "r")
        self.library_f = open(os.path.join(self.file_path, "resources", "library.txt"), "r")
        self.library_entrance_f = open(os.path.join(self.file_path, "resources", "library_entrance.txt"), "r")
        self.east_room_f = open(os.path.join(self.file_path, "resources", "east_room.txt"), "r")
        self.throne_entrance_f = open(os.path.join(self.file_path, "resources", "throne_entrance.txt"), "r")
        self.hidden_room_f = open(os.path.join(self.file_path, "resources", "hidden_room.txt"), "r")
        self.throne_room_f = open(os.path.join(self.file_path, "resources", "throne_room.txt"), "r")

        # configure the name and author of the game
        RPGInfo.author = "Timo Früh"
        RPGInfo.title = "The Chosen"
        RPGInfo.subtitle = "At Nights End"

        # set welcome message to the content of the text file loaded above
        RPGInfo.welcome_message = self.welcome_f.read()

        # initialise all rooms and set their description to the corresponding text file
        self.cellar = Room(room_name="Cellar")
        self.cellar.set_desc(self.cellar_f.read())

        self.cellar_ladder = Room(room_name="Ladder to the Cellar")
        self.cellar_ladder.set_desc(self.cellar_ladder_f.read())

        self.hall = Room(room_name="The Hall")
        self.hall.set_desc(self.hall_f.read())

        self.west_room = Room(room_name="Room West to the Hall")
        self.west_room.set_desc(self.west_room_f.read())

        self.trophy_room = Room(room_name="Trophy Room")
        self.trophy_room.set_desc(self.trophy_room_f.read())

        self.ns_passageway = Room(room_name="N/S Passageway")
        self.ns_passageway.set_desc(self.ns_passageway_f.read())

        self.staff_room = Room(room_name="Staff Room")
        self.staff_room.set_desc(self.staff_room_f.read())

        self.library = Room(room_name="The Library")
        self.library.set_desc(self.library_f.read())

        self.library_entrance = Room(room_name="Library Entrance")
        self.library_entrance.set_desc(self.library_entrance_f.read())

        self.east_room = Room(room_name="Room East to the Hall")
        self.east_room.set_desc(self.east_room_f.read())

        self.throne_entrance = Room(room_name="Entrance to the Throne Room")
        self.throne_entrance.set_desc(self.throne_entrance_f.read())

        self.hidden_room = Room(room_name="Hidden Room")
        self.hidden_room.set_desc(self.hidden_room_f.read())

        self.throne_room = Room(room_name="The Throne Room")
        self.throne_room.set_desc(self.throne_room_f.read())

        # connect all the rooms
        self.cellar_up_ladder = Ladder({Dh.UP: self.cellar_ladder, Dh.DOWN: self.cellar})
        self.cl_north_door = Door({Dh.NORTH: self.hall, Dh.SOUTH: self.cellar_ladder}, isopen=True)
        self.hall_west_door = Door({Dh.WEST: self.west_room, Dh.EAST: self.hall}, isopen=True)
        self.wr_west_door = Door({Dh.WEST: self.trophy_room, Dh.EAST: self.west_room}, isopen=True)
        self.tr_north_door = Door({Dh.NORTH: self.ns_passageway, Dh.SOUTH: self.trophy_room}, isopen=True)
        self.ns_north_door = Door({Dh.NORTH: self.staff_room, Dh.SOUTH: self.ns_passageway}, isopen=True)
        self.sr_east_door = Door({Dh.EAST: self.library, Dh.WEST: self.staff_room}, isopen=True)
        self.lb_south_door = Door({Dh.SOUTH: self.library_entrance, Dh.NORTH: self.library}, isopen=True)
        self.le_south = Door({Dh.SOUTH: self.hall, Dh.NORTH: self.library_entrance}, isopen=True)
        self.hall_east_door = Door({Dh.EAST: self.east_room, Dh.WEST: self.hall}, isopen=True)
        self.er_east_door = Door({Dh.EAST: self.throne_entrance, Dh.WEST: self.east_room}, isopen=True)
        self.throne_door = Door({Dh.NORTH: self.throne_room, Dh.SOUTH: self.throne_entrance}, isopen=True)
        self.illusory_wall = IllusoryWall({Dh.SOUTH: self.hidden_room, Dh.NORTH: self.throne_entrance})

        # initialise all items, set their (initial) description and their initial room
        self.longsword = Item(art="a", item_name="sword")
        self.longsword.set_description("a simple one, but it seems like good craftsmanship.")
        self.cellar.add_item(self.longsword)

        self.crossbow = Item(art="a", item_name="crossbow")
        self.crossbow.set_description("double-winged and small. It looks magical, "
                                      "probably enchanted to shoot infinite bolts.")
        self.cellar.add_item(self.crossbow)

        self.swords_odd = Artifacts(art="the", item_name="Swords of Dusk and Dawn", initial_room=self.hidden_room)
        self.swords_odd.add_alias("swords")
        self.swords_odd.set_description("both faintly glowing.")
        self.swords_odd.set_initial_description("resting in a wooden case, both shining brilliantly, "
                                                "Dusk silver and Dawn crimson.")
        self.hidden_room.add_item(self.swords_odd)

        self.candle = Item(art="a", item_name="candle")
        self.candle.set_description("standing on the ground, its flame flickering.")
        self.hall.add_item(self.candle)

        self.water_bottle = Item(art="a", item_name="bottle of holy water")
        self.water_bottle.add_alias("holy water")
        self.water_bottle.add_alias("bottle")
        self.water_bottle.add_alias("water")
        self.water_bottle.set_description("standing on the ground.")
        self.library.add_item(self.water_bottle)

        # print welcome message
        RPGInfo.welcome()

        # prompt the player for a name
        self.player_name = input("What is your name? ")

        # set player name to "Stranger" if none was provided
        if self.player_name.replace(" ", "") == "":
            self.player_name = "Stranger"

        # initialise the player, set their name to the prevously configured player name
        # and set their starting room to the cellar
        self.player = Player(player_name=self.player_name, starting_room=self.cellar)

        # initialise all mobs and their weaknesses
        self.fire_demon = Mob(class_name="demon of fire")
        self.fire_demon.add_weakness(self.swords_odd)
        self.fire_demon.add_weakness(self.water_bottle)
        self.west_room.add_character(self.fire_demon)

        self.fire_demon2 = Mob(class_name="demon of fire")
        self.fire_demon2.add_weakness(self.swords_odd)
        self.fire_demon2.add_weakness(self.water_bottle)
        self.east_room.add_character(self.fire_demon2)

        self.water_demon = Mob(class_name="demon of water")
        self.water_demon.add_weakness(self.swords_odd)
        self.water_demon.add_weakness(self.candle)
        self.trophy_room.add_character(self.water_demon)

        self.water_demon2 = Mob(class_name="demon of water")
        self.water_demon2.add_weakness(self.swords_odd)
        self.water_demon2.add_weakness(self.candle)
        self.library_entrance.add_character(self.water_demon2)

        self.earth_demon = Mob(class_name="demon of earth")
        self.earth_demon.add_weakness(self.swords_odd)
        self.earth_demon.add_weakness(self.longsword)
        self.ns_passageway.add_character(self.earth_demon)

        self.earth_demon2 = Mob(class_name="demon of earth")
        self.earth_demon2.add_weakness(self.swords_odd)
        self.earth_demon2.add_weakness(self.longsword)
        self.library.add_character(self.earth_demon)

        self.air_demon = Mob(class_name="demon of air")
        self.air_demon.add_weakness(self.swords_odd)
        self.air_demon.add_weakness(self.crossbow)
        self.staff_room.add_character(self.air_demon)

        self.air_demon2 = Mob(class_name="demon of air")
        self.air_demon2.add_weakness(self.swords_odd)
        self.air_demon2.add_weakness(self.crossbow)
        self.hall.add_character(self.air_demon2)

        # initialise all characters, their descriptions, conversations, rooms and weaknesses
        # and define whether they are able to kill the player
        self.elliot = Friend(character_name="Elliot")
        self.elliot.set_desc("a man you've never seen before. Or have you? How else would you know his name?")
        self.elliot.set_conversation(f"\tHey, {self.player_name}! Long time no see! Have you heard the latest gossip?\n"
                                     "\t\tWe all know that the Demon King can be killed with the legendary Swords, right?\n"
                                     "\t\tRumour has it that even with those you'd have to kill seven of\n"
                                     "\t\this demons first, to weaken him.\n"
                                     "\t\tBut what do I know!")
        self.west_room.add_character(self.elliot)

        self.scholar = Stranger(class_name="scholar", deadly=False)
        self.scholar.set_desc("currently searching for some book somewhere on the shelves.")
        self.scholar.set_conversation("\tHello my son. Are you in need of a book?\n"
                                      "\t\tI'm sorry, but I'm afraid the library doesn't hand them over to strangers.")
        self.library.add_character(self.scholar)

        self.hag = Stranger(class_name="old hag", deadly=False)
        self.hag.add_alias("hag")
        self.hag.set_desc("sitting on the bed.")
        self.hag.set_conversation("\tOooh ... what a fine surprise ... the Chosen is finally here. You know\n"
                                  "\t\tyour task already, I suppose? Quick, quick, let me tell you something then:\n"
                                  "\t\tTo discover the swords you must find the three burning suns, then turn\n"
                                  "\t\tsouth and take the daring step.\n"
                                  "\t\tThat doesn't help you? Well, this is all I know.")
        self.staff_room.add_character(self.hag)

        self.stranger = Stranger(class_name="stranger", deadly=True)
        self.stranger.set_desc("leaning on the far end of the wall, examining you with cold, blue eyes.")
        self.stranger.set_conversation("Hm. Another one. The world is going mad .... And what do you do?\n"
                                       "\t\tWaving around your sword as if you were able to do something.\n"
                                       "\t\tThis is all pointless!")
        self.hall.add_character(self.stranger)

        self.warrioress = Stranger(class_name="warrioress", deadly=True)
        self.warrioress.set_desc("seeming a bit lost but eying you with obvious distrust.")
        self.ns_passageway.add_character(self.warrioress)

        self.mandrak = Enemy(character_name="Mandrak")
        self.mandrak.add_alias("servant")
        self.mandrak.set_desc("a servant of the Demon King, standing firm in front of the Throne Room, holding his lance close.")
        self.mandrak.set_conversation("\tTurn back, oh powerless soul. I will let you pass, but He will\n"
                                      "\t\tkill you if you try to take his throne.\n"
                                      "\t\tLong live the Demon King!")
        self.mandrak.add_weakness(self.swords_odd)
        self.throne_entrance.add_character(self.mandrak)

        self.demon_king = Endboss(character_name="An-Harat", title="Demon King", kills_needed=7)
        self.demon_king.set_desc("sitting on his magnificent throne and looking incredibly menacing.")
        self.demon_king.set_conversation("\tAah, greetings, Chosen. You are here at last.\n"
                                         "\t\tWhat took you so long? My demons certainly were no challenge for you,\n"
                                         "\t\tfor you are in the posession of the legendary Swords of Dusk and Dawn.\n"
                                         "\t\tEven as powerful a servant as Mandrak would not have been able to withstand\n"
                                         "\t\tthose dreadful blades of yours, the bringers of death and destruction.\n"
                                         "\t\tAre you here to kill me, then? Do you want to take my throne?\n"
                                         "\t\tYou want to take my world from me, because you think it belongs to you mortals?\n"
                                         "\t\tYou want to end my eternal reign and rid the world of my kind?\n"
                                         "\t\tCome on then, try to ban me from my realm, try to destroy my immortal soul\n"
                                         "\t\twith these weapons you carry and I'll behead you right where you stand!")
        self.demon_king.add_weakness(self.swords_odd)
        self.throne_room.add_character(self.demon_king)

        # print "You look around." and a empty line after that
        print("\nYou look around.")
        print("")

        # print the details of the current room
        self.player.get_current_room().describe()

    # define the mainloop method, which is essentially where the magic happens
    def mainloop(self):

        # set alive to true (it can later be set to false to end the game)
        alive = True

        # set victory to false (it can later be set to true to end the game and display a victory message)
        victory = False

        # repeat the program until alive becomes false or victory becomes true
        while alive and not victory:

            # display a command prompt for the user
            print("")
            user_input = input("> ")

            # set the command variable to the users input, make it all lowecase and remove spaces from end and beginning
            command = user_input.lower().strip()

            # if the command is "commands" or "help" or "?" execute the print_commands() method from the Commands class
            if command in ["commands", "help", "?"]:
                Cmd.print_commands()

            # if the command is a direction execute the movement() method from the Commands class
            elif command in ["north", "east", "south", "west", "up", "down"]:
                self.player.move(command)

            # if the command is "look" or "l" execute the look() method from the Commands class
            elif command in ["look", "l"]:
                self.player.look()

            # if the player writes "talk to" instead of "talk" do the same as if they wrote "talk"
            elif "talk to" in command:

                # interpret positional command "talk to ..."
                talk_to_input = InputInterpreter.interpret_single(command, "talk to")

                # execute the talk() method from the Commands class
                self.player.talk(talk_to_input)

            # if "talk" is in the command do the following
            elif "talk" in command:

                # interpret positional command "talk ..."
                talk_input = InputInterpreter.interpret_single(command, "talk")

                # execute the talk() method from the Commands class
                self.player.talk(talk_input)

            # if the command is "inventory" or "i" or "backpack" execute the show_inventory() method from the Commands class
            elif command in ["inventory", "i", "backpack"]:
                self.player.show_inventory()

            # if "fight" is in the command and the player is currently in the throne room do the following
            elif "fight" in command and self.player.get_current_room() == self.throne_room:

                # interpret positional command "fight ... with ..."
                boss_fight_input = InputInterpreter.interpret_double(command, "fight", "with")

                # execute the fight() method from the Commands class and put its output into the boss_fight variable
                self.player.fight(whom=boss_fight_input[0], item=boss_fight_input[1])

            # if "fight" is in the command do the following
            elif "fight" in command:

                # interpret positional command "fight ... with ...
                fight_input = InputInterpreter.interpret_double(command, "fight", "with")

                # execute the fight() method from the Commands class
                self.player.fight(whom=fight_input[0], item=fight_input[1])

            # if "take" is in the command do the following
            elif "take" in command:

                # interpret positional command "talk ..."
                take_input = InputInterpreter.interpret_single(command, "take")

                # execute the take() method from the Commands class
                self.player.take(take_input)

            # if "drop" is in the command do the following
            elif "drop" in command:

                # interpret positional command "drop ..."
                drop_input = InputInterpreter.interpret_single(command, "drop")

                # execute the drop() method from the Commands class
                self.player.drop(drop_input)

            # if "hug" is in the command do the following
            elif "hug" in command:

                # interpret the positional command "hug ..."
                hug_input = InputInterpreter.interpret_single(command, "hug")

                # execute the hug() method from the Commands class
                self.player.hug(hug_input)

            # if the command is "quit" or "exit"
            elif command in ["quit", "exit"]:

                # execute the quit() method from the Commands class and set its output to the confirm variable
                confirm = Cmd.quit()

                # end the game if confirmation was given
                if confirm:
                    alive = False

            # if the command is empty pass on
            elif command == "":
                pass

            # if the command was none of the above print an error message
            else:
                print(f"I do not know what you meant by {user_input}.")

            # end the game if the player has died
            if not self.player.isalive():
                alive = False

            # end the game if the player has killed the endboss
            if self.player.haswon():
                victory = True

        # print a victory message if victory is true after the end of the loop
        if victory:
            print("\nCongratulations! You have been victorious and thereby beaten the game!\n")

        # print kill message (depending on how many the user scored)
        if self.player.get_kills() == 0:
            print(f"You vanquished not a single enemy during the game.")
        elif self.player.get_kills() == 1:
            print(f"You vanquished 1 enemy during the game.")
        elif self.player.get_kills() > 1:
            print(f"You vanquished {self.player.get_kills()} enemies during the game.")

        # print an empty line after the kill message
        print("")

        if victory:
            # print the credits
            RPGInfo.credits()

            # print an empty line after the credits
            print("")

        # print a message to hit enter to exit the game
        input("[Hit enter to exit.]")

        # clear the screen again after the end of the game
        clear()


# define a main() function in which the Main class and its mainloop() method are called
def main():
    game = Main()

    game.mainloop()


# run the game if it is started from this file
# (only to be used through pyinstaller or somesuch, use ../the-chosen.py instead)
if __name__ == "__main__":
    main()
