from os import CLD_CONTINUED


class Link:
    def __init__(self, connect_1, connect_2):
        self.connections = [connect_1, connect_2]

    def get_connections(self):
        return self.connections


class Door(Link):
    def __init__(self, isopen, connect_1, connect_2):
        super().__init__(connect_1, connect_2)
        self.open = isopen
    
    def open(self):
        self.open = True
        print("You opened the door.")

    def close(self):
        self.open = False
        print("You closed the door.")
    
    def isopen(self):
        return self.open


class Ladder(Link):
    def __init__(self, connect_1, connect_2):
        super().__init__(connect_1, connect_2)
