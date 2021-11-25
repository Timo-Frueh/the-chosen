class DirectionHelper:

    NORTH = "north"
    EAST = "east"
    SOUTH = "south"
    WEST = "west"
    UP = "up"
    DOWN = "down"

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
        elif direction == cls.UP:
            return cls.DOWN
        elif direction == cls.DOWN:
            return cls.UP
