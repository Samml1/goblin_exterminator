import random
from classStructure import player, room

# Create Dungeon entrance
entrance = room('Dungeon Entrance', 'The Entrance to the dungeon')

# Create Test player instance if user does not run new game command
user1 = player("TestPlayer", 'entrance')

# create a new player object when called from the main loop
def newPlayer():
    global user1
    userName = input("What is your name?\n")

    user1 = player(userName, 'entrance')

    print("Welcome to your Adventure, " + user1.name + "!")

    return user1

def createDungeon(dungeonName):
    global roomList

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

def randomEncounter():
    # Create a chance of a random encounter occurring
    encounterChance = random.randint(0, 100)

    if user1.location.enemyRoom:
        if 0 < encounterChance < 30:
            print("you find an empty room")
        elif 30 < encounterChance < 90:
            print("You find  goblin")
        else:
            print("You encounter the king goblin")


def playerMove(playerAction):
    # player movement logic
    if playerAction in user1.location.exits:
        user1.location = user1.location.exits[playerAction]
        print("You go {} and find yourself in a ".format(playerAction) + user1.location.roomName)
        print(user1.location.roomName)
        randomEncounter()
    else:
        print("Unable to move in that direction\n")

def dungeonExplore():
    global roomList

    dungeonName = input("Whch dungeon would you like to explore: \ngoblin cave \n").lower()
    createDungeon(dungeonName)

    user1.location = roomList[0]
    print("You stand at the entrance to the Dungeon")

    while True:
        playerAction = input("What would you like to do next\n").lower()

        # handle player movement
        if playerAction in ["north","east","south","west"]:
            playerMove(playerAction)

        if playerAction == "describe":
            print(user1.location.description)
            for key in (user1.location.exits.keys()):
                print("There is an exit: " + key)

        if playerAction == "location":
            print(user1.location.roomName)

        if playerAction == "exit":
            if user1.location.roomName == "Dungeon Entrance":
                print("You leave the dungeon\n")
                break
            else:
                print("You cannot leave from here, please return to entrance\n")

        if playerAction.lower() == 'q':
            exit()

while True:
    playerAction = input("What would you like to do?\n").lower()

    #Instantiate a new Game and create the player class
    if playerAction == "new game":
        newPlayer()

    #Instantiate a dungeon instance and let the player explore
    if playerAction == "enter dungeon":
        dungeonExplore()

    if playerAction == "view stats":
        print(user1.name)

    if playerAction.lower() == 'q':
        exit()
