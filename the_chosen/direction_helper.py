# coding=utf-8

# The Chosen  Copyright (C) 2021  Timo Früh
# Full copyright notice in main.py

class DirectionHelper:

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
