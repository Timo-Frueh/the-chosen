from the_chosen.direction_helper import DirectionHelper as Dr


class Link:
    def __init__(self, rooms):
        self.connections = []

        for direction in rooms:
            self.add_connection(rooms[direction])
            rooms[direction].add_link(Dr.reverse_dir(direction), self)

        self.open = True

    def get_connections(self):
        return self.connections

    def add_connection(self, room):
        if len(self.connections) <= 2:
            self.connections.append(room)
        else:
            raise Exception("A link cannot have more than two connections.")

    def get_other_room(self, room):
        if room == self.connections[0]:
            return self.connections[1]
        elif room == self.connections[1]:
            return self.connections[0]


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


class IllusoryWall(Link):
    def __init__(self, rooms):
        super().__init__(rooms)
