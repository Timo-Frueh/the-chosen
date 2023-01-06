# coding=utf-8

"""
This module holds the Link class and all its subclasses.

Classes:
    Link
    Door
    Ladder
    IllusoryWall
"""

# The Chosen  Copyright (C) 2021-2023  Timo Früh
# Full copyright notice in __main__.py

import the_chosen.io as io
from the_chosen.direction_helper import DirectionHelper as Dr


class Link:
    """
    This is the base class for links which are here to connect rooms.
    """

    def __init__(self, rooms):
        self.connections = []
        self.message = None

        for direction in rooms:
            self.add_connection(rooms[direction])
            rooms[direction].add_link(Dr.reverse_dir(direction), self)

    def get_connections(self):
        """
        Return the rooms the link connects.

        :return: The list of rooms the link connects.
        :rtype: list
        """
        return self.connections

    def add_connection(self, room):
        """
        Add a connecting room to the door.

        :param room: The room to be connected.
        """

        if len(self.connections) < 2:
            self.connections.append(room)
        else:
            raise Exception("A link cannot have more than two connections.")

    def get_other_room(self, room):
        """
        Get the opposite room of the input.

        :param room: The room the opposite if wanted of.
        :type room: Room

        :return: The opposite room of the one in the room parameter.
        :rtype: Room
        """

        if room == self.connections[0]:
            return self.connections[1]
        elif room == self.connections[1]:
            return self.connections[0]

    def open_door(self):
        """
        Open the link.
        Prints an error message because normal links cannot be opened or closed.
        """

        io.ch_print("This cannot be opened, because it is no door.")

    def unlock_door(self, key):  # pylint: disable=unused-argument
        """
        Unlock the link with a key.
        Prints an error message because normal links cannot be locked or unlocked.
        """

        io.ch_print("This cannot be unlocked, because it is no door.")

    def close_door(self):
        """
        Close the link.
        Prints an error message because normal links cannot be opened or closed.
        """

        io.ch_print("This cannot be opened, because it is no door.")

    def lock_door(self, key):  # pylint: disable=unused-argument
        """
        Lock the link.
        Prints an error message because normal links cannot be opened or closed.
        """

        io.ch_print("This cannot be closed, because it is no door.")

    def isopen(self):
        """
        Check whether a link is open.
        Returns true because normal links are always open.
        """

        return True

    def print_message(self, direction):
        """
        Print the correct pass-through message for the specified direction.
        Does nothing because only ladders and illusory walls have pass-through messages.
        """

        pass


class Door(Link):
    def __init__(self, rooms, isopen=True, islocked=False):
        super().__init__(rooms)
        self.open = isopen
        self.locked = islocked
        self.keys = []
    
    def open_door(self):
        """
        Open the door.
        """

        if not self.locked:
            self.open = True
            io.ch_print("You open the door.")
        else:
            io.ch_print("This door is locked.")

    def unlock_door(self, key):
        """
        Unlock the door with a key.

        :param key: The key the door is to be unlocked with.
        :type key: Item
        """

        if self.open:
            io.ch_print("You cannot unlock an open door.")
        elif not self.locked:
            io.ch_print("This door is already unlocked.")
        elif not self.keys:
            io.ch_print("This door has no lock.")
        else:
            if key in self.keys:
                self.locked = False
                key.print_unlock_message()
            elif type(key).__name__ == "Key":
                io.ch_print("This key doesn't fit into the keyhole.")
            else:
                io.ch_print(f"You can't unlock a door with {key.get_art_name()}.")

    def close_door(self):
        """
        Close the door.
        """

        if not self.locked:
            self.open = False
            io.ch_print("You close the door.")
        else:
            raise Exception("An open door cannot be open and locked at the same time.")

    def lock_door(self, key):
        """
        Lock the door with a key.

        :param key: The key the door is to be locked with.
        :type key: Item
        """

        if self.open:
            io.ch_print("You cannot lock an open door.")
        elif self.locked:
            io.ch_print("This door is already locked.")
        elif not self.keys:
            io.ch_print("This door has no lock.")
        else:
            if key in self.keys:
                self.locked = True
                key.print_lock_message()
            elif type(key).__name__ == "Key":
                io.ch_print("This key doesn't fit into the keyhole.")
            else:
                io.ch_print(f"You can't lock a door with {key.get_art_name()}.")
    
    def isopen(self):
        """
        Check whether a door is open.

        :return: True if open, false if closed.
        :rtype: bool
        """

        return self.open

    def islocked(self):
        """
        Check whether a door is locked.

        :return: True if locked, false if unlocked.
        :rtype: bool
        """

        return self.locked

    def add_key(self, key):
        """
        Add a key the door should be able to be opened with.

        :param key: The key to add to the keys list.
        :type key: Item
        """

        self.keys.append(key)

    def get_keys(self):
        """
        Return all the keys of the door in a list.

        :return: All the keys of the door.
        :rtype: str
        """

        return self.keys


class Ladder(Link):
    """
    This is the class for ladders which display a message if climbed.
    """

    def print_message(self, direction):
        """
        Print a climb message depending on the direction.

        :param direction: The direction the player is climbing to.
        :type direction: str
        """

        io.ch_print(f"You climb {direction} the ladder.\n")


class IllusoryWall(Link):
    """
    This is the class for illusory walls, which do not appear in a room's description and print a message when
    traversed.
    """

    def print_message(self, direction):
        """
        Print a pass-through message depending on the direction.

        :param direction: The direction wall is to from the player's perspective.
        :type direction: str
        """

        io.ch_print(f"As you lay your hand upon the {direction} wall, you pass through it and emerge on the other side.\n")
