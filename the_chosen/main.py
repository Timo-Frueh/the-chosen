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

import os

from clear_screen import clear

from the_chosen.character import Endboss, Friend, Miniboss, Mob, Stranger
from the_chosen.commands import Commands as Cmd
from the_chosen.direction_helper import DirectionHelper as Dh
from the_chosen.input_interpreter import InputInterpreter
from the_chosen.item import Artifacts, Weapon, Key
from the_chosen.link import Door, IllusoryWall, Ladder
from the_chosen.player import Player
from the_chosen.resource_helper import ResourceHelper as Rh
from the_chosen.room import Room
from the_chosen.rpginfo import RPGInfo


class Main:
    def __init__(self):

        # clear the screen at the beginning of the game
        clear()

        # load all room description files and the welcome message file
        self.file_path = os.path.dirname(os.path.abspath(__file__))
        Rh.set_resources_path(os.path.join(self.file_path, "resources"))

        self.welcome_f = Rh.read_resource("welcome_message.txt")
        self.cellar_f = Rh.read_resource("cellar.txt")
        self.cellar_ladder_f = Rh.read_resource("cellar_ladder.txt")
        self.hall_f = Rh.read_resource("hall.txt")
        self.west_room_f = Rh.read_resource("west_room.txt")
        self.trophy_room_f = Rh.read_resource("trophy_room.txt")
        self.ns_passageway_f = Rh.read_resource("ns_passageway.txt")
        self.staff_room_f = Rh.read_resource("staff_room.txt")
        self.library_f = Rh.read_resource("library.txt")
        self.library_entrance_f = Rh.read_resource("library_entrance.txt")
        self.east_room_f = Rh.read_resource("east_room.txt")
        self.throne_entrance_f = Rh.read_resource("throne_entrance.txt")
        self.hidden_room_f = Rh.read_resource("hidden_room.txt")
        self.throne_room_f = Rh.read_resource("throne_room.txt")

        self.longsword_f = Rh.read_resource("longsword.txt")
        self.crossbow_f = Rh.read_resource("crossbow.txt")
        self.swords_odd_f = Rh.read_resource("swords_odd.txt")
        self.swords_odd_init_f = Rh.read_resource("swords_odd_init.txt")
        self.fire_wand_f = Rh.read_resource("fire_wand.txt")
        self.holy_water_f = Rh.read_resource("holy_water.txt")
        self.key_f = Rh.read_resource("key.txt")

        self.elliot_f = Rh.read_resource("elliot.txt")
        self.elliot_con_f = Rh.read_resource("elliot_con.txt")
        self.scholar_f = Rh.read_resource("scholar.txt")
        self.scholar_con_f = Rh.read_resource("scholar_con.txt")
        self.hag_f = Rh.read_resource("hag.txt")
        self.hag_con_f = Rh.read_resource("hag_con.txt")
        self.stranger_f = Rh.read_resource("stranger.txt")
        self.stranger_con_f = Rh.read_resource("stranger_con.txt")
        self.warrioress_f = Rh.read_resource("warrioress.txt")
        self.mandrak_f = Rh.read_resource("mandrak.txt")
        self.mandrak_con_f = Rh.read_resource("mandrak_con.txt")
        self.demon_king_f = Rh.read_resource("demon_king.txt")
        self.demon_king_con_f = Rh.read_resource("demon_king_con.txt")
        self.demon_king_hug_f = Rh.read_resource("demon_king_hug.txt")
        self.demon_king_kill_f = Rh.read_resource("demon_king_kill.txt")

        self.air_demon_kill_f = Rh.read_resource("air_demon_kill.txt")
        self.earth_demon_kill_f = Rh.read_resource("earth_demon_kill.txt")
        self.water_demon_kill_f = Rh.read_resource("water_demon_kill.txt")
        self.fire_demon_kill_f = Rh.read_resource("fire_demon_kill.txt")

        self.longsword_kill_f = Rh.read_resource("longsword_kill.txt")
        self.crossbow_kill_f = Rh.read_resource("crossbow_kill.txt")
        self.holy_water_kill_f = Rh.read_resource("holy_water_kill.txt")
        self.fire_wand_kill_f = Rh.read_resource("fire_wand_kill.txt")

        # configure the name and author of the game
        RPGInfo.author = "Timo Früh"
        RPGInfo.title = "The Chosen"
        RPGInfo.subtitle = "At Nights End"

        # set welcome message to the content of the text file loaded above
        RPGInfo.welcome_message = self.welcome_f

        # initialise all rooms and set their description to the corresponding text file
        self.cellar = Room(room_name="Cellar")
        self.cellar.set_desc(self.cellar_f)

        self.cellar_ladder = Room(room_name="Ladder to the Cellar")
        self.cellar_ladder.set_desc(self.cellar_ladder_f)

        self.hall = Room(room_name="The Hall")
        self.hall.set_desc(self.hall_f)

        self.west_room = Room(room_name="Room West to the Hall")
        self.west_room.set_desc(self.west_room_f)

        self.trophy_room = Room(room_name="Trophy Room")
        self.trophy_room.set_desc(self.trophy_room_f)

        self.ns_passageway = Room(room_name="N/S Passageway")
        self.ns_passageway.set_desc(self.ns_passageway_f)

        self.staff_room = Room(room_name="Staff Room")
        self.staff_room.set_desc(self.staff_room_f)

        self.library = Room(room_name="The Library")
        self.library.set_desc(self.library_f)

        self.library_entrance = Room(room_name="Library Entrance")
        self.library_entrance.set_desc(self.library_entrance_f)

        self.east_room = Room(room_name="Room East to the Hall")
        self.east_room.set_desc(self.east_room_f)

        self.throne_entrance = Room(room_name="Entrance to the Throne Room")
        self.throne_entrance.set_desc(self.throne_entrance_f)

        self.hidden_room = Room(room_name="Hidden Room")
        self.hidden_room.set_desc(self.hidden_room_f)

        self.throne_room = Room(room_name="The Throne Room")
        self.throne_room.set_desc(self.throne_room_f)

        self.key = Key(art="a", name="key")
        self.key.set_description("made of brass.")
        self.cellar.add_item(self.key)

        # connect all the rooms
        self.cellar_up_ladder = Ladder({Dh.UP: self.cellar_ladder, Dh.DOWN: self.cellar})

        self.cl_north_door = Door({Dh.NORTH: self.hall, Dh.SOUTH: self.cellar_ladder}, isopen=False, islocked=True)
        self.cl_north_door.add_key(self.key)

        self.hall_west_door = Door({Dh.WEST: self.west_room, Dh.EAST: self.hall})
        self.wr_west_door = Door({Dh.WEST: self.trophy_room, Dh.EAST: self.west_room})
        self.tr_north_door = Door({Dh.NORTH: self.ns_passageway, Dh.SOUTH: self.trophy_room})
        self.ns_north_door = Door({Dh.NORTH: self.staff_room, Dh.SOUTH: self.ns_passageway})
        self.sr_east_door = Door({Dh.EAST: self.library, Dh.WEST: self.staff_room})
        self.lb_south_door = Door({Dh.SOUTH: self.library_entrance, Dh.NORTH: self.library})
        self.le_south = Door({Dh.SOUTH: self.hall, Dh.NORTH: self.library_entrance})
        self.hall_east_door = Door({Dh.EAST: self.east_room, Dh.WEST: self.hall})
        self.er_east_door = Door({Dh.EAST: self.throne_entrance, Dh.WEST: self.east_room})
        self.throne_door = Door({Dh.NORTH: self.throne_room, Dh.SOUTH: self.throne_entrance})
        self.illusory_wall = IllusoryWall({Dh.SOUTH: self.hidden_room, Dh.NORTH: self.throne_entrance})

        # initialise all items, set their (initial) description and their initial room
        self.longsword = Weapon(art="a", name="sword")
        self.longsword.set_description(self.longsword_f)
        self.longsword.set_kill_message(self.longsword_kill_f)
        self.cellar.add_item(self.longsword)

        self.crossbow = Weapon(art="a", name="crossbow")
        self.crossbow.set_description(self.crossbow_f)
        self.crossbow.set_kill_message(self.crossbow_kill_f)
        self.cellar.add_item(self.crossbow)

        self.swords_odd = Artifacts(item_name="Swords of Dusk and Dawn", initial_room=self.hidden_room)
        self.swords_odd.add_alias("swords")
        self.swords_odd.set_description(self.swords_odd_f)
        self.swords_odd.set_initial_description(self.swords_odd_init_f)
        self.hidden_room.add_item(self.swords_odd)

        self.fire_wand = Weapon(art="a", name="wand of fire")
        self.fire_wand.add_alias("wand")
        self.fire_wand.add_alias("fire")
        self.fire_wand.set_description(self.fire_wand_f)
        self.fire_wand.set_kill_message(self.fire_wand_kill_f)
        self.hall.add_item(self.fire_wand)

        self.holy_water = Weapon(art="a", name="bottle of holy water")
        self.holy_water.add_alias("holy water")
        self.holy_water.add_alias("bottle")
        self.holy_water.add_alias("water")
        self.holy_water.set_kill_message(self.holy_water_kill_f)
        self.holy_water.set_description(self.holy_water_f)
        self.library.add_item(self.holy_water)

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
        self.fire_demon = Mob(art="a", character_name="demon of fire")
        self.fire_demon.add_weakness(self.swords_odd)
        self.fire_demon.add_weakness(self.holy_water)
        self.fire_demon.add_alias("fire demon")
        self.fire_demon.set_kill_message(self.fire_demon_kill_f)
        self.west_room.add_character(self.fire_demon)

        self.fire_demon2 = Mob(art="a", character_name="demon of fire")
        self.fire_demon2.add_weakness(self.swords_odd)
        self.fire_demon2.add_weakness(self.holy_water)
        self.fire_demon2.add_alias("fire demon")
        self.fire_demon2.set_kill_message(self.fire_demon_kill_f)
        self.east_room.add_character(self.fire_demon2)

        self.water_demon = Mob(art="a", character_name="demon of water")
        self.water_demon.add_weakness(self.swords_odd)
        self.water_demon.add_weakness(self.fire_wand)
        self.water_demon.add_alias("water demon")
        self.water_demon.set_kill_message(self.water_demon_kill_f)
        self.trophy_room.add_character(self.water_demon)

        self.water_demon2 = Mob(art="a", character_name="demon of water")
        self.water_demon2.add_weakness(self.swords_odd)
        self.water_demon2.add_weakness(self.fire_wand)
        self.water_demon2.add_alias("water demon")
        self.water_demon2.set_kill_message(self.water_demon_kill_f)
        self.library_entrance.add_character(self.water_demon2)

        self.earth_demon = Mob(art="a", character_name="demon of earth")
        self.earth_demon.add_weakness(self.swords_odd)
        self.earth_demon.add_weakness(self.longsword)
        self.earth_demon.add_alias("earth demon")
        self.earth_demon.set_kill_message(self.earth_demon_kill_f)
        self.ns_passageway.add_character(self.earth_demon)

        self.earth_demon2 = Mob(art="a", character_name="demon of earth")
        self.earth_demon2.add_weakness(self.swords_odd)
        self.earth_demon2.add_weakness(self.longsword)
        self.earth_demon2.add_alias("earth demon")
        self.earth_demon2.set_kill_message(self.earth_demon_kill_f)
        self.library.add_character(self.earth_demon)

        self.air_demon = Mob(art="a", character_name="demon of air")
        self.air_demon.add_weakness(self.swords_odd)
        self.air_demon.add_weakness(self.crossbow)
        self.air_demon.add_alias("air demon")
        self.air_demon.set_kill_message(self.air_demon_kill_f)
        self.staff_room.add_character(self.air_demon)

        self.air_demon2 = Mob(art="a", character_name="demon of air")
        self.air_demon2.add_weakness(self.swords_odd)
        self.air_demon2.add_weakness(self.crossbow)
        self.air_demon2.add_alias("air demon 2")
        self.air_demon2.set_kill_message(self.air_demon_kill_f)
        self.hall.add_character(self.air_demon2)

        # initialise all characters, their descriptions, conversations, rooms and weaknesses
        # and define whether they are able to kill the player
        self.elliot = Friend(character_name="Elliot")
        self.elliot.set_description(self.elliot_f)
        self.elliot.set_conversation(f"Hey, {self.player_name}!\n" + self.elliot_con_f)
        self.west_room.add_character(self.elliot)

        self.scholar = Stranger(art="a", class_name="scholar", deadly=False)
        self.scholar.set_description(self.scholar_f)
        self.scholar.set_conversation(self.scholar_con_f)
        self.library.add_character(self.scholar)

        self.hag = Stranger(art="an", class_name="old hag", deadly=False)
        self.hag.add_alias("hag")
        self.hag.set_description(self.hag_f)
        self.hag.set_conversation(self.hag_con_f)
        self.staff_room.add_character(self.hag)

        self.stranger = Stranger(art="a", class_name="stranger", deadly=True)
        self.stranger.set_description(self.stranger_f)
        self.stranger.set_conversation(self.stranger_con_f)
        self.hall.add_character(self.stranger)

        self.warrioress = Stranger(art="a", class_name="warrioress", deadly=True)
        self.warrioress.set_description(self.warrioress_f)
        self.ns_passageway.add_character(self.warrioress)

        self.mandrak = Miniboss(character_name="Mandrak")
        self.mandrak.add_alias("servant")
        self.mandrak.set_description(self.mandrak_f)
        self.mandrak.set_conversation(self.mandrak_con_f)
        self.mandrak.add_weakness(self.swords_odd)
        self.throne_entrance.add_character(self.mandrak)

        self.demon_king = Endboss(character_name="An-Harat", title="Demon King", kills_needed=7)
        self.demon_king.set_description(self.demon_king_f)
        self.demon_king.set_conversation(self.demon_king_con_f)
        self.demon_king.add_weakness(self.swords_odd)
        self.demon_king.set_hug_message(self.demon_king_hug_f)
        self.demon_king.set_kill_message(self.demon_king_kill_f)
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
            elif command in Dh.DIRECTIONS:
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
                boss_fight_input = InputInterpreter.interpret_double(command, "fight", "with", [", "])

                # execute the fight() method from the Commands class and put its output into the boss_fight variable
                self.player.fight(character=boss_fight_input[0], item=boss_fight_input[1])

            # if "fight" is in the command do the following
            elif "fight" in command:

                # interpret positional command "fight ... with ...
                fight_input = InputInterpreter.interpret_double(command, "fight", "with", [", "])

                # execute the fight() method from the Commands class
                self.player.fight(character=fight_input[0], item=fight_input[1])

            # if "take" is in the command do the following
            elif "take" in command:

                # interpret positional command "talk ..."
                take_input = InputInterpreter.interpret_single(command, "take")

                # execute the take() method from the Commands class
                self.player.take(take_input)

            # if "drop" is in the command do the following
            elif "drop" in command:

                # interpret positional command "drop ..."
                drop_input = InputInterpreter.interpret_single(command, "drop", [])

                # execute the drop() method from the Commands class
                self.player.drop(drop_input)

            # if "hug" is in the command do the following
            elif "hug" in command:

                # interpret the positional command "hug ..."
                hug_input = InputInterpreter.interpret_single(command, "hug")

                # execute the hug() method from the Commands class
                self.player.hug(hug_input)

            elif "open" in command:
                open_with_input = InputInterpreter.interpret_double(command, "open", "with", [" the ", " door"])
                self.player.open_door(direction=open_with_input[0], key=open_with_input[1])

            elif "close" in command:
                close_with_input = InputInterpreter.interpret_double(command, "close", "with", [" the ", " door"])
                self.player.close_door(direction=close_with_input[0], key=close_with_input[1])

            elif "unlock" in command:
                unlock_input = InputInterpreter.interpret_double(command, "unlock", "with", [" the ", " door"])
                self.player.unlock_door(direction=unlock_input[0], key=unlock_input[1])

            elif "lock" in command:
                lock_input = InputInterpreter.interpret_double(command, "lock", "with", [" the ", " door"])
                self.player.lock_door(direction=lock_input[0], key=lock_input[1])

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
            print("You vanquished not a single enemy during the game.")
        elif self.player.get_kills() == 1:
            print("You vanquished 1 enemy during the game.")
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
