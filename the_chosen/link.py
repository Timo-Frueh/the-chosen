# coding=utf-8

# The Chosen  Copyright (C) 2021  Timo Früh
# Full copyright notice in main.py

from the_chosen.direction_helper import DirectionHelper as Dr


class Link:
    def __init__(self, rooms):
        self.connections = []
        self.message = None

        for direction in rooms:
            self.add_connection(rooms[direction])
            rooms[direction].add_link(Dr.reverse_dir(direction), self)

    def get_connections(self):
        return self.connections

    def add_connection(self, room):
        if len(self.connections) < 2:
            self.connections.append(room)
        else:
            raise Exception("A link cannot have more than two connections.")

    def get_other_room(self, room):
        if room == self.connections[0]:
            return self.connections[1]
        elif room == self.connections[1]:
            return self.connections[0]

    def open_door(self):
        print("This cannot be opened, because it is no door.")

    def unlock_door(self, key): # pylint: disable=unused-argument
        print("This cannot be unlocked, because it is no door.")

    def close_door(self):
        print("This cannot be opened, because it is no door.")

    def lock_door(self, key): # pylint: disable=unused-argument
        print("This cannot be closed, because it is no door.")

    def isopen(self):
        return True

    def print_message(self, direction):
        pass


class Door(Link):
    def __init__(self, rooms, isopen, islocked):
        super().__init__(rooms)
        self.open = isopen
        self.locked = islocked
        self.keys = []
    
    def open_door(self):
        if not self.locked:
            self.open = True
            print("You open the door.")
        else:
            print("This door is locked.")

    def unlock_door(self, key):
        if self.open:
            print("You cannot unlock an open door.")
        elif not self.locked:
            print("This door is already unlocked.")
        elif not self.keys:
            print("This door has no lock.")
        else:
            if key in self.keys:
                self.locked = False
                print("You unlock the door.")
            else:
                print("You cannot unlock the door with this.")

    def close_door(self):
        if not self.locked:
            self.open = False
            print("You close the door.")
        else:
            raise Exception("An open door cannot be open and locked at the same time.")

    def lock_door(self, key):
        if self.open:
            print("You cannot lock an open door.")
        elif self.locked:
            print("This door is already locked.")
        elif not self.keys:
            print("This door has no lock.")
        else:
            if key in self.keys:
                self.locked = True
                print("You lock the door.")
            else:
                print("You cannot lock the door with this.")
    
    def isopen(self):
        return self.open

    def islocked(self):
        return self.locked

    def add_key(self, key):
        self.keys.append(key)

    def get_keys(self):
        return self.keys


class Ladder(Link):

    def print_message(self, direction):
        print(f"You climb {direction} the ladder.\n")


class IllusoryWall(Link):
    
    def print_message(self, direction):
        print(f"As you lay your hand upon the {direction} wall, you pass through it and emerge on the other side.\n")
