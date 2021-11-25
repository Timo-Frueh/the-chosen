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
            rooms[direction].init_links()

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

    def close_door(self):
        print("This cannot be opened, because it is no door.")

    def isopen(self):
        return True

    def print_message(self, direction):
        pass


class Door(Link):
    def __init__(self, rooms, isopen):
        super().__init__(rooms)
        self.open = isopen
    
    def open_door(self):
        self.open = True
        print("You opened the door.")

    def close_door(self):
        self.open = False
        print("You closed the door.")
    
    def isopen(self):
        return self.open


class Ladder(Link):
    def __init__(self, rooms):
        super().__init__(rooms)

    def print_message(self, direction):
        print(f"You climb {direction} the ladder.\n")


class IllusoryWall(Link):
    def __init__(self, rooms):
        super().__init__(rooms)

    def print_message(self, direction):
        print(f"As you lay your hand upon the {direction} wall, you pass through it and emerge on the other side.\n")
