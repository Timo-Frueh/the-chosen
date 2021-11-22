class Door:
    def __init__(self, isopen, con_from, con_to):
        self.open = isopen
        self.connect_from = con_from
        self.connect_to = con_to
    
    def pass_through(self, current_room):
        pass
