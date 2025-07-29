from classStructure import room

# create a new dungeon instance as a list of room objects
def createDungeon(dungeonName):

    if dungeonName == "goblin cave":
        # Create the dungeon rooms
        entrance = room('Dungeon Entrance', 'The Entrance to the dungeon')
        hallway = room('Dungeon hallway', 'A dark wet hallway that smells of mildew')
        treasureRoom = room('Treasure Room', 'A room full of a horde of treasure')

        # Create exits
        entrance.exits["north"] = hallway
        hallway.exits["south"] = entrance
        hallway.exits["east"] = treasureRoom
        treasureRoom.exits["west"] = hallway

        # Create enemy rooms
        entrance.enemyRoom = False
        hallway.enemyRoom = False
        treasureRoom.enemyRoom = True

        roomList = [entrance, hallway, treasureRoom]
    elif dungeonName == "q":
        exit()
    else:
        dungeonName = input("No dungeon by that name found\nplease enter name again\n")
        createDungeon(dungeonName)

    return roomList
