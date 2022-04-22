# coding=utf-8

"""
This module holds the DirectionHelper class.
"""

# The Chosen  Copyright (C) 2022  Timo Früh
# Full copyright notice in __main__.py


class DirectionHelper:
    """
    This class helps managing directions.
    """

    NORTH = "north"
    EAST = "east"
    SOUTH = "south"
    WEST = "west"
    UP = "up"
    DOWN = "down"

    DIRECTIONS = [NORTH, EAST, SOUTH, WEST, UP, DOWN]
    HORIZ_DIRECTIONS = [NORTH, EAST, SOUTH, WEST]
    VERT_DIRECTIONS = [UP, DOWN]

    @classmethod
    def reverse_dir(cls, direction):
        """
        Return the reverse direction of the input.

        :param direction: The direction the revers direction is wanted of.
        :type direction: str

        :return: The reverse direction of the input.
        :rtype: str
        """

        if direction == cls.NORTH:
            return cls.SOUTH
        elif direction == cls.EAST:
            return cls.WEST
        elif direction == cls.SOUTH:
            return cls.NORTH
        elif direction == cls.WEST:
            return cls.EAST
        elif direction == cls.UP:
            return cls.DOWN
        elif direction == cls.DOWN:
            return cls.UP
