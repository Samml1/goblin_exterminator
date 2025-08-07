import yaml
import io
from yaml.loader import SafeLoader
from classStructure import room
from functools import reduce
roomList = []

# Take dungeon name and open YML file
def yamlReader(fileName):
    # open yaml file for loading
    with open(fileName + '.yml', 'r') as f:
        data = list(yaml.load_all(f, Loader=SafeLoader))

    return data

# from room.exits dict transform string values into pointers to objects they represent
def createExits(roomlist):
    for i in range(0, len(roomList)):
        for j in range(0,len(roomList)):
            if roomList[j].name in roomList[i].exits.values():
                for x in roomList[i].exits:
                    if roomList[i].exits[x] == roomList[j].name:
                        roomList[i].exits[x] = roomList[j]


# Create the rooms for the dungeon
def createRoom(roomId, roomName, description, enemyRoom, exits, items):
    # from provided yaml data create object room
    roomId = room(roomId, roomName, description)
    roomId.enemyRoom = enemyRoom
    roomId.exits = exits
    roomId.items = items

    # create list of rooms to be called on later
    roomList.append(roomId)

    return roomList

# Print the values as a dictionary
def defineDungeon(data):
    #Loop list of yaml data entries
    for i in range(0,len(data)):

        room = data[i].get('room')
        roomName = data[i].get('roomName')
        description = data[i].get('description')
        enemyRoom = bool(data[i].get('enemyRoom'))
        exits = data[i].get('exits', {})
        exits = reduce(lambda union, next_dict: union.update(next_dict) or union, exits, {})

        items = data[i].get('items', {})
        if items != None:
            items = reduce(lambda union, next_dict: union.update(next_dict) or union, items, {})

        #pass each yaml data entry to function
        createRoom(room, roomName, description, enemyRoom, exits, items)

# Call this function from main.py to run through creation process
def munchYaml(fileName):
    data = yamlReader(fileName)
    defineDungeon(data)
    createExits(data)

    return roomList
