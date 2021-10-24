from the_chosen.rpginfo import RPGInfo
from the_chosen.room import Room
from the_chosen.player import Player
from the_chosen.character import Stranger, Friend, Enemy, Boss, Mob
from the_chosen.commands import Commands as Cmd
from the_chosen.item import Item, Artifacts
from the_chosen.input_interpreter import InputInterpreter

import os
from clear_screen import clear


class Main:
    def __init__(self):

        clear()

        self.file_path = os.path.dirname(os.path.abspath(__file__))
        self.welcome_f = open(os.path.join(self.file_path, "resources", "welcome_message.txt"), "r")
        self.cellar_f = open(os.path.join(self.file_path, "resources", "cellar.txt"), "r")
        self.stairwell_f = open(os.path.join(self.file_path, "resources", "stairwell.txt"), "r")
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

        RPGInfo.author = "Timo Früh"
        RPGInfo.title = "The Chosen"
        RPGInfo.subtitle = "At Nights End"

        RPGInfo.welcome_message = self.welcome_f.read()

        self.cellar = Room(room_name="Cellar")
        self.cellar.set_desc(self.cellar_f.read())

        self.stairwell = Room(room_name="Stairwell to the Cellar")
        self.stairwell.set_desc(self.stairwell_f.read())

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

        self.hall.link_room(direction="east", room=self.east_room)
        self.east_room.link_room(direction="west", room=self.hall)

        self.east_room.link_room(direction="east", room=self.throne_entrance)
        self.throne_entrance.link_room(direction="west", room=self.east_room)

        self.throne_entrance.link_room(direction="north", room=self.throne_room)

        self.throne_entrance.link_hidden(direction="south", room=self.hidden_room)
        self.hidden_room.link_hidden(direction="north", room=self.throne_entrance)

        self.longsword = Item(art="a", item_name="sword")
        self.longsword.set_description("a simple longsword, but it seems like good craftsmanship.")
        self.cellar.add_item(self.longsword)

        self.crossbow = Item(art="a", item_name="crossbow")
        self.crossbow.set_description("double-winged and small. It looks magical, probably enchanted to shoot infinite bolts.")
        self.cellar.add_item(self.crossbow)

        self.swords_odd = Artifacts(art="the", item_name="Swords of Dusk and Dawn", initial_room=self.hidden_room)
        self.swords_odd.set_description("both faintly glowing.")
        self.swords_odd.set_initial_description("resting in a wooden case, both shining brilliantly, "
                                                "Dusk silver and Dawn crimson.")
        self.hidden_room.add_item(self.swords_odd)

        self.candle = Item(art="a", item_name="candle")
        self.candle.set_description("standing on the ground, its flame flickering.")
        self.hall.add_item(self.candle)

        self.water_bottle = Item(art="a", item_name="bottle of holy water")
        self.water_bottle.set_description("standing on the ground.")
        self.library.add_item(self.water_bottle)

        RPGInfo.welcome()

        self.player_name = input("What is your name? ")
        if self.player_name.replace(" ", "") == "":
            self.player_name = "Stranger"
        self.player = Player(player_name=self.player_name, starting_room=self.cellar)

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
        self.hag.set_desc("sitting on the bed.")
        self.hag.set_conversation("\tOooh ... what a fine surprise ... the Chosen is finally here. You know\n"
                                  "\t\tyour task already, I suppose? Quick, quick, let me tell you something then:\n"
                                  "\t\tTo discover the swords you must find the three burning suns, then turn\n"
                                  "\t\tto ice and take the daring step.\n"
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

        self.gatekeeper = Enemy(character_name="The Gatekeeper")
        self.gatekeeper.set_desc("standing firm in front of the Throne Room, holding his lance close.")
        self.gatekeeper.set_conversation("\tTurn back, oh powerless soul. I will let you pass, but He will\n"
                                         "\t\t\tkill you if you try to take his throne.\n"
                                         "\t\t\tLong live the Demon King!")
        self.gatekeeper.add_weakness(self.swords_odd)
        self.throne_entrance.add_character(self.gatekeeper)

        self.demon_king = Boss(character_name="An-Harat", kills_needed=7)
        self.demon_king.set_desc("the Demon King, sitting on his magnificent throne and looking incredibly menacing.")
        self.demon_king.set_conversation("\tI know you're here to kill me.\n"
                                         "\t\t\tSo let's just skip the talking part and start to FIGHT!")
        self.demon_king.add_weakness(self.swords_odd)
        self.throne_room.add_character(self.demon_king)

        print("\nYou look around.")

        print("")

        self.player.get_current_room().describe()

    def mainloop(self):

        alive = True
        victory = False

        while alive and not victory:
            print("")
            user_input = input("> ")
            command = user_input.lower().replace(" ", "")

            if command in ["commands", "help", "?"]:
                Cmd.print_commands()

            elif command in ["north", "east", "south", "west"]:
                Cmd.movement(self.player, command)

            elif command in ["look", "l"]:
                Cmd.look(self.player)

            elif "talk" in command:
                talk_input = InputInterpreter.interpret_single(command, "talk")
                Cmd.talk(self.player, talk_input)

            elif command in ["inventory", "i", "backpack"]:
                Cmd.show_inventory(self.player)

            elif "fight" in command and self.player.get_current_room() == self.throne_room:
                boss_fight_input = InputInterpreter.interpret_double(command, "fight", "with")
                boss_fight = Cmd.fight(self.player, who=boss_fight_input[0], item=boss_fight_input[1])
                alive = boss_fight["alive"]
                victory = boss_fight["victory"]

            elif "fight" in command:
                fight_input = InputInterpreter.interpret_double(command, "fight", "with")
                alive = Cmd.fight(self.player, who=fight_input[0], item=fight_input[1])["alive"]

            elif "take" in command:
                take_input = InputInterpreter.interpret_single(command, "take")
                Cmd.take(self.player, take_input)

            elif "drop" in command:
                drop_input = InputInterpreter.interpret_single(command, "drop")
                Cmd.drop(self.player, drop_input)

            elif "hug" in command:
                hug_input = InputInterpreter.interpret_single(command, "hug")
                Cmd.hug(self.player, hug_input)

            elif command in ["quit", "exit"]:
                confirm = Cmd.quit()
                if confirm == "y":
                    alive = False

            elif command == "":
                pass

            else:
                print(f"I do not know what you meant by {user_input}.")

        if victory:
            print("\nCongratulations! You have been victorious and thereby beaten the game!\n")

        if self.player.get_kills() == 0:
            print(f"You vanquished not a single enemy during the game.")
        elif self.player.get_kills() == 1:
            print(f"You vanquished 1 enemy during the game.")
        elif self.player.get_kills() > 1:
            print(f"You vanquished {self.player.get_kills()} enemies during the game.")

        print("")
        RPGInfo.credits()
        print("")

        input("[Hit enter to exit.]")
        clear()


def main():
    game = Main()

    game.mainloop()


if __name__ == "__main__":
    main()
