class player(object):
    def __init__(self, name, location):
        self.name = name
        self.location = location

class room(object):
    def __init__(self, roomName, description):
        self.roomName = roomName
        self. description = description
        self.exits = {}
        self.enemies = {}
        self.enemyRoom = False
