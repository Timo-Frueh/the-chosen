class Player:
    def __init__(self, player_name, starting_room):
        self.name = player_name
        self.inventory = []
        self.current_room = starting_room

    def get_name(self):
        return self.name

    def get_current_room(self):
        return self.current_room

    def move(self, direction):
        if direction in self.current_room.get_linked_rooms():
            self.current_room = self.current_room.get_linked_rooms()[direction]
        else:
            print("You can't go that way")
            print("")