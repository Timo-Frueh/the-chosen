class Link:
    def __init__(self, connect_1, connect_2):
        self.connections = [connect_1, connect_2]

    def get_connections(self):
        return self.connections

    def get_other_room(self, room):
        if room == self.connections[0]:
            return self.connections[1]
        elif room == self.connections[1]:
            return self.connections[0]


class Door(Link):
    def __init__(self, isopen, connect_1, connect_2):
        super().__init__(connect_1, connect_2)
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
    def __init__(self, connect_1, connect_2):
        super().__init__(connect_1, connect_2)
