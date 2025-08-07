class player(object):
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.playerHP = int('10')
        self.holdingWeapon = False
        self.playerHeldWeapon = ""
        self.inventory = []

class room(object):
    def __init__(self, name, roomName, description):
        self.name = name
        self.roomName = roomName
        self.description = description
        self.enemyRoom = bool()
        self.items = {}
        self.exits = {}

class item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.isWeapon = False

class weapon(item):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.minDamage = int()
        self.maxDamage = int()
