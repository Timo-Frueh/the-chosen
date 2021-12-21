# coding=utf-8

# The Chosen  Copyright (C) 2021  Timo Früh
# Full copyright notice in main.py

from the_chosen.direction_helper import DirectionHelper as Dh


class Player:

    def __init__(self, player_name, starting_room):
        self.name = player_name
        self.inventory = []
        self.current_room = starting_room
        self.alive = True
        self.kills = 0
        self.victory = False

    def move(self, direction):

        move = direction.lower().strip()
        link = self.current_room.get_link(move)

        if not link and move in Dh.HORIZ_DIRECTIONS:
            print("You run head first into a wall and realize: You can't go that way.")
        elif not link and move == Dh.UP:
            print("You jump. Nothing happens. What did you expect?")
        elif not link and move == Dh.DOWN:
            print("You kneel down and examine the floor. There doesn't seem to be a way down.")
        elif not link:
            print("You can't go that way.")
        elif not link.isopen():
            print(f"The door to the {direction} is closed.")
        else:
            link.print_message(move)
            self.current_room = link.get_other_room(self.current_room)
            self.current_room.describe()

    def look(self):

        self.get_current_room().describe()

    def talk(self, character):

        if character.strip() == "":
            user_input = input("Talk to whom? ")
        else:
            user_input = character

        talk_to = user_input.lower().strip()
        character = self.current_room.get_character(talk_to)

        if not self.current_room.get_characters():
            print("There is no one here to listen to your beautiful voice.")
        elif not character:
            print(f"There is no one called {user_input} here.")
        else:
            character.talk()
            
    def show_inventory(self):

        if self.get_inventory():
            print("You are carrying:")
            for item in self.get_inventory():
                print(f"- {item.get_c_art_name()}")

        else:
            print("You are empty-handed.")
    
    def fight(self, character, item):

        if character.strip() == "":
            user_input = input("Fight whom? ")
        else:
            user_input = character
        
        fight = user_input.lower().strip()
        enemy = self.current_room.get_character(fight)

        if enemy and item.strip() == "":
            user_input_2 = input("What do you want to fight with? ")
        elif enemy and item.strip() != "":
            user_input_2 = item
        else:
            user_input_2 = ""
        
        fight_with = user_input_2.lower().strip()
        weapon = self.get_inventory_item(fight_with)

        if not self.current_room.get_characters():
            print("There is no one here to fight.")
        elif not enemy:
            print(f"There is no one called {user_input} here.")
        elif not weapon:
            print(f"You do not have an item called {user_input_2}.")
        else:
            enemy.fight(weapon, self)
    
    def take(self, item):

        if item.strip() == "":
            user_input = input("What do you want to take? ")
        else:
            user_input = item
        
        take = user_input.lower().strip()
        item = self.current_room.get_item(take)

        if not self.current_room.get_items():
            print("There is nothing here to take.")
        elif not item:
            print(f"There is no item called {user_input} here.")
        else:
            self.current_room.remove_item(item)
            self.add_to_inventory(item)
            print("Taken.")

    def drop(self, item):

        if item.strip() == "":
            user_input = input("What do you want to drop? ")
        else:
            user_input = item
        
        drop = user_input.lower().strip()
        item = self.get_inventory_item(drop)

        if not self.inventory:
            print("You do not have anything to drop.")
        elif not item:
            print(f"You do not have an item called {user_input}.")
        else:
            self.remove_from_inventory(item)
            self.current_room.add_item(item)
            print("Dropped.")
    
    def hug(self, character):

        if character.strip() == "":
            user_input = input("Hug whom? ")
        else:
            user_input = character

        hug = user_input.lower().strip()
        character = self.current_room.get_character(hug)

        if not self.current_room.get_characters():
            print("There is no one here to receive your comforting embrace.")
        elif not character:
            print(f"There is no one called {user_input} here.")
        else:
            character.hug()
                
    def open_door(self, direction, key):

        if direction.strip() == "":
            user_input = input("Open door to which direction? ")
        else:
            user_input = direction

        open_door = user_input.lower().strip()
        open_with = key.lower().strip()
        door = self.current_room.get_link(open_door)
        key = self.get_inventory_item(open_with)

        if open_door not in Dh.HORIZ_DIRECTIONS:
            print("You need to specify a direction so I know which door you mean.")
        elif not door:
            print(f"There is no door to the {user_input}.")
        elif key:
            door.unlock_door(key)
            door.open_door()
        else:
            door.open_door()

    def unlock_door(self, direction, key):
        
        if direction.strip() == "":
            user_input = input("Unlock door to which direction? ")
        else:
            user_input = direction

        unlock_door = user_input.lower().strip()
        door = self.current_room.get_link(unlock_door)

        if door and key.strip() == "":
            user_input_2 = input("Which key do you want to use? ")
        elif door and key.strip() != "":
            user_input_2 = key
        else:
            user_input_2 = ""

        unlock_with = user_input_2.lower().strip()
        key = self.get_inventory_item(unlock_with)
        
        if unlock_door not in Dh.HORIZ_DIRECTIONS:
            print("You need to specify a direction so I know which door you mean.")
        elif not door:
            print(f"There is no door to the {user_input}.")
        elif not key:
            print(f"You do not have an item called {user_input_2}.")
        else:
            door.unlock_door(key)

    def close_door(self, direction, key):

        if direction.strip() == "":
            user_input = input("Open door to which direction? ")
        else:
            user_input = direction

        close_door = user_input.lower().strip()
        close_with = key.lower().strip()
        door = self.current_room.get_link(close_door)
        key = self.get_inventory_item(close_with)

        if close_door not in Dh.HORIZ_DIRECTIONS:
            print("You need to specify a direction so I know which door you mean.")
        elif not door:
            print(f"There is no door to the {user_input}.")
        elif key:
            door.close_door()
            door.lock_door(key)
        else:
            door.close_door()

    def lock_door(self, direction, key):
        
        if direction.strip() == "":
            user_input = input("Lock door to which direction? ")
        else:
            user_input = direction

        lock_door = user_input.lower().strip()
        door = self.current_room.get_link(lock_door)

        if door and key.strip() == "":
            user_input_2 = input("Which key do you want to use? ")
        elif door and key.strip() != "":
            user_input_2 = key
        else:
            user_input_2 = ""

        lock_with = user_input_2.lower().strip()
        key = self.get_inventory_item(lock_with)
        
        if lock_door not in Dh.HORIZ_DIRECTIONS:
            print("You need to specify a direction so I know which door you mean.")
        elif not door:
            print(f"There is no door to the {user_input}.")
        elif door.islocked():
            print(f"You do not have an item called {user_input_2}.")
        else:
            door.lock_door(key)

    def get_inventory(self):
        return self.inventory

    def get_inventory_item(self, name):
        for item in self.inventory:
            if name.lower().strip() in item.get_aliases():
                return item

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def remove_from_inventory(self, item):
        self.inventory.remove(item)

    def get_name(self):
        return self.name

    def get_current_room(self):
        return self.current_room

    def isalive(self):
        return self.alive

    def die(self):
        self.alive = False

    def get_kills(self):
        return self.kills

    def add_kill(self):
        self.kills += 1

    def haswon(self):
        return self.victory

    def win(self):
        self.victory = True
