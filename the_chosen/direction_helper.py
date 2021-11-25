class DirectionHelper:

    NORTH = "north"
    EAST = "east"
    SOUTH = "south"
    WEST = "west"

    @classmethod
    def reverse_dir(cls, direction):
        if direction == cls.NORTH:
            return cls.SOUTH
        elif direction == cls.EAST:
            return cls.WEST
        elif direction == cls.SOUTH:
            return cls.NORTH
        elif direction == cls.EAST:
            return cls.EAST
