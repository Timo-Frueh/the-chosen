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
from the_chosen.direction_helper import DirectionHelper as Dh
from the_chosen.item import Artifacts, Key, Weapon
from the_chosen.link import Door, IllusoryWall, Ladder
from the_chosen.mainloop import Mainloop as Ml
from the_chosen.player import Player
from the_chosen.resource_helper import ResourceHelper as Rh
from the_chosen.room import Room
from the_chosen.rpginfo import RPGInfo


class Main:
    def __init__(self):

        clear()

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
        self.swords_odd_req_msg_f = Rh.read_resource("swords_odd_req_msg.txt")
        self.fire_wand_f = Rh.read_resource("fire_wand.txt")
        self.holy_water_f = Rh.read_resource("holy_water.txt")
        self.key_f = Rh.read_resource("key.txt")
        self.key_unlock_f = Rh.read_resource("key_unlock.txt")

        self.elliot_f = Rh.read_resource("elliot.txt")
        self.elliot_con_f = Rh.read_split_resource("elliot_con.txt")
        self.scholar_f = Rh.read_resource("scholar.txt")
        self.scholar_con_f = Rh.read_split_resource("scholar_con.txt")
        self.hag_f = Rh.read_resource("hag.txt")
        self.hag_con_f = Rh.read_split_resource("hag_con.txt")
        self.stranger_f = Rh.read_resource("stranger.txt")
        self.stranger_con_f = Rh.read_split_resource("stranger_con.txt")
        self.warrioress_f = Rh.read_resource("warrioress.txt")
        self.warrioress_con_f = Rh.read_split_resource("warrioress_con.txt")
        self.mandrak_f = Rh.read_resource("mandrak.txt")
        self.mandrak_con_f = Rh.read_split_resource("mandrak_con.txt")
        self.demon_king_f = Rh.read_resource("demon_king.txt")
        self.demon_king_con_f = Rh.read_split_resource("demon_king_con.txt")
        self.demon_king_hug_f = Rh.read_resource("demon_king_hug.txt")
        self.demon_king_kill_f = Rh.read_resource("demon_king_kill.txt")

        self.air_demon_kill_f = Rh.read_resource("air_demon_kill.txt")
        self.earth_demon_kill_f = Rh.read_resource("earth_demon_kill.txt")
        self.water_demon_kill_f = Rh.read_resource("water_demon_kill.txt")
        self.water_demon_hw_kill_f = Rh.read_resource("water_demon_holy_water_kill.txt")
        self.fire_demon_kill_f = Rh.read_resource("fire_demon_kill.txt")

        self.longsword_kill_f = Rh.read_resource("longsword_kill.txt")
        self.crossbow_kill_f = Rh.read_resource("crossbow_kill.txt")
        self.holy_water_kill_f = Rh.read_resource("holy_water_kill.txt")
        self.fire_wand_kill_f = Rh.read_resource("fire_wand_kill.txt")
        self.fire_wand_wd_kill_f = Rh.read_resource("fire_wand_water_demon_kill.txt")

        RPGInfo.author = "Timo Früh"
        RPGInfo.title = "The Chosen"
        RPGInfo.subtitle = "At Nights End"

        RPGInfo.welcome_message = self.welcome_f

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
        self.key.set_description(self.key_f)
        self.key.set_unlock_message(self.key_unlock_f)
        self.cellar.add_item(self.key)

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

        self.longsword = Weapon(art="a", name="sword")
        self.longsword.set_description(self.longsword_f)
        self.longsword.set_def_kill_message(self.longsword_kill_f)
        self.cellar.add_item(self.longsword)

        self.crossbow = Weapon(art="a", name="crossbow")
        self.crossbow.set_description(self.crossbow_f)
        self.crossbow.set_def_kill_message(self.crossbow_kill_f)
        self.cellar.add_item(self.crossbow)

        self.swords_odd = Artifacts(item_name="Swords of Dusk and Dawn", initial_room=self.hidden_room)
        self.swords_odd.add_alias("swords")
        self.swords_odd.set_description(self.swords_odd_f)
        self.swords_odd.set_initial_description(self.swords_odd_init_f)
        self.swords_odd.set_no_req_message(self.swords_odd_req_msg_f)
        self.hidden_room.add_item(self.swords_odd)

        self.fire_wand = Weapon(art="a", name="wand of fire")
        self.fire_wand.add_alias("wand")
        self.fire_wand.add_alias("fire")
        self.fire_wand.set_description(self.fire_wand_f)
        self.fire_wand.set_def_kill_message(self.fire_wand_kill_f)
        self.fire_wand.set_kill_message("demon of water", self.fire_wand_wd_kill_f)
        self.hall.add_item(self.fire_wand)

        self.holy_water = Weapon(art="a", name="bottle of holy water")
        self.holy_water.add_alias("holy water")
        self.holy_water.add_alias("bottle")
        self.holy_water.add_alias("water")
        self.holy_water.set_def_kill_message(self.holy_water_kill_f)
        self.holy_water.set_description(self.holy_water_f)
        self.library.add_item(self.holy_water)

        RPGInfo.welcome()

        self.player_name = input("What is your name? ")

        if self.player_name.replace(" ", "") == "":
            self.player_name = "Stranger"

        self.player = Player(player_name=self.player_name, starting_room=self.cellar)
        self.swords_odd.set_kills_req(7)

        self.fire_demon = Mob(art="a", character_name="demon of fire")
        self.fire_demon.add_weakness(self.swords_odd)
        self.fire_demon.add_weakness(self.holy_water)
        self.fire_demon.add_alias("fire demon")
        self.fire_demon.set_def_kill_message(self.fire_demon_kill_f)
        self.west_room.add_character(self.fire_demon)

        self.fire_demon2 = Mob(art="a", character_name="demon of fire")
        self.fire_demon2.add_weakness(self.swords_odd)
        self.fire_demon2.add_weakness(self.holy_water)
        self.fire_demon2.add_alias("fire demon")
        self.fire_demon2.set_def_kill_message(self.fire_demon_kill_f)
        self.east_room.add_character(self.fire_demon2)

        self.water_demon = Mob(art="a", character_name="demon of water")
        self.water_demon.add_weakness(self.swords_odd)
        self.water_demon.add_weakness(self.fire_wand)
        self.water_demon.add_alias("water demon")
        self.water_demon.set_def_kill_message(self.water_demon_kill_f)
        self.water_demon.set_kill_message("bottle of holy water", self.water_demon_hw_kill_f)
        self.trophy_room.add_character(self.water_demon)

        self.water_demon2 = Mob(art="a", character_name="demon of water")
        self.water_demon2.add_weakness(self.swords_odd)
        self.water_demon2.add_weakness(self.fire_wand)
        self.water_demon2.add_alias("water demon")
        self.water_demon2.set_def_kill_message(self.water_demon_kill_f)
        self.water_demon2.set_kill_message("bottle of holy water", self.water_demon_hw_kill_f)
        self.library_entrance.add_character(self.water_demon2)

        self.earth_demon = Mob(art="a", character_name="demon of earth")
        self.earth_demon.add_weakness(self.swords_odd)
        self.earth_demon.add_weakness(self.longsword)
        self.earth_demon.add_alias("earth demon")
        self.earth_demon.set_def_kill_message(self.earth_demon_kill_f)
        self.ns_passageway.add_character(self.earth_demon)

        self.earth_demon2 = Mob(art="a", character_name="demon of earth")
        self.earth_demon2.add_weakness(self.swords_odd)
        self.earth_demon2.add_weakness(self.longsword)
        self.earth_demon2.add_alias("earth demon")
        self.earth_demon2.set_def_kill_message(self.earth_demon_kill_f)
        self.library.add_character(self.earth_demon)

        self.air_demon = Mob(art="a", character_name="demon of air")
        self.air_demon.add_weakness(self.swords_odd)
        self.air_demon.add_weakness(self.crossbow)
        self.air_demon.add_alias("air demon")
        self.air_demon.set_def_kill_message(self.air_demon_kill_f)
        self.staff_room.add_character(self.air_demon)

        self.air_demon2 = Mob(art="a", character_name="demon of air")
        self.air_demon2.add_weakness(self.swords_odd)
        self.air_demon2.add_weakness(self.crossbow)
        self.air_demon2.add_alias("air demon")
        self.air_demon2.set_def_kill_message(self.air_demon_kill_f)
        self.hall.add_character(self.air_demon2)

        self.elliot = Friend(character_name="Elliot")
        self.elliot.set_description(self.elliot_f)
        self.elliot.add_conversation(f"Hey, {self.player_name}!\n" + self.elliot_con_f[0])
        self.elliot.add_conversation(self.elliot_con_f[1])
        self.west_room.add_character(self.elliot)

        self.scholar = Stranger(art="a", class_name="scholar", deadly=False)
        self.scholar.set_description(self.scholar_f)
        self.scholar.add_conversation(self.scholar_con_f[0])
        self.scholar.add_conversation(self.scholar_con_f[1])
        self.library.add_character(self.scholar)

        self.hag = Stranger(art="an", class_name="old hag", deadly=False)
        self.hag.add_alias("hag")
        self.hag.set_description(self.hag_f)
        self.hag.add_conversation(self.hag_con_f[0])
        self.hag.add_conversation(self.hag_con_f[1])
        self.hag.add_conversation(self.hag_con_f[2])
        self.staff_room.add_character(self.hag)

        self.stranger = Stranger(art="a", class_name="stranger", deadly=True)
        self.stranger.set_description(self.stranger_f)
        self.stranger.add_conversation(self.stranger_con_f[0])
        self.stranger.add_conversation(self.stranger_con_f[1])
        self.stranger.add_conversation(self.stranger_con_f[2])
        self.hall.add_character(self.stranger)

        self.warrioress = Stranger(art="a", class_name="warrioress", deadly=True)
        self.warrioress.set_description(self.warrioress_f)
        self.warrioress.add_conversation(self.warrioress_con_f[0])
        self.warrioress.add_conversation(self.warrioress_con_f[1])
        self.warrioress.add_conversation(self.warrioress_con_f[0])
        self.ns_passageway.add_character(self.warrioress)

        self.mandrak = Miniboss(character_name="Mandrak")
        self.mandrak.add_alias("servant")
        self.mandrak.set_description(self.mandrak_f)
        self.mandrak.add_conversation(self.mandrak_con_f[0])
        self.mandrak.add_conversation(self.mandrak_con_f[1])
        self.mandrak.add_weakness(self.swords_odd)
        self.throne_entrance.add_character(self.mandrak)

        self.demon_king = Endboss(character_name="An-Harat", title="Demon King")
        self.demon_king.set_description(self.demon_king_f)
        self.demon_king.add_conversation(self.demon_king_con_f[0])
        self.demon_king.add_conversation(self.demon_king_con_f[1])
        self.demon_king.add_weakness(self.swords_odd)
        self.demon_king.set_hug_message(self.demon_king_hug_f)
        self.demon_king.set_def_kill_message(self.demon_king_kill_f)
        self.throne_room.add_character(self.demon_king)

        print("\nYou look around.")
        print("")

        self.player.get_current_room().describe()

    def main(self):

        Ml.mainloop(self.player)

        clear()


def main():
    game = Main()

    game.main()


if __name__ == "__main__":
    main()
