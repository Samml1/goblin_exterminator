import random
from createDungeonYML import *
from initialisePlayer import *
roomList = []
startingItems = []

# Create Test player instance if user does not run new game command
user1 = player("TestPlayer", 'entrance')

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
        print(user1.location.description)
        randomEncounter()
    else:
        print("Unable to move in that direction\n")

def dungeonExplore():

    dungeonName = input("Whch dungeon would you like to explore: \ngoblin cave \n").lower()

    # Deprecated method for creating dungeons
    '''roomList = createDungeon(dungeonName)'''

    # Current dungeon creation method
    dungeonName = dungeonName.replace(" ","_")
    roomList = munchYaml(dungeonName)

    # Set user to position 0 in roomList - this should be dungeon entrance
    user1.location = roomList[0]
    print("You stand at the entrance to the Dungeon")

    # Loop for player actions in dungeon
    while True:
        playerAction = input("What would you like to do next\n").lower()

        # handle player movement
        if playerAction.lower() in ["north","east","south","west"]:
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

#Main gameplay loop
while True:

    #Instantiate a new Game and create the player class
    if user1.name == 'TestPlayer':
        user1 = newPlayer()
        startingItems = giveStartingItems()
        user1.inventory = startingItems

    #Get the player input and loop
    playerAction = input("What would you like to do?\n").lower()

    #Instantiate a dungeon instance and let the player explore
    if playerAction == "enter dungeon":
        dungeonExplore()

    #View the user stats
    if playerAction == "view stats":
        print("Player Name: " + user1.name)
        print("HP: " + str(user1.playerHP))
        print("Inventory:")
        for i in range(0, len(user1.inventory)):
            print("    " + user1.inventory[i].name + ": " + user1.inventory[i].description, user1.inventory[i].isWeapon)
        if user1.holdingWeapon:
            print("Equipped Weapon: " + user1.playerHeldWeapon.name, user1.playerHeldWeapon.description)
        else:
            print("Equipped Weapon: None")

    if playerAction == "equip weapon":
        weaponChange = False
        weaponSelect = input("equip which weapon?\n").lower()
        for i in range(0,len(user1.inventory)):
            if weaponSelect == user1.inventory[i].name.lower():
                weaponSelect = user1.inventory[i]
                equipWeapon(weaponSelect, user1)
                break


    # instantiate new player instace upong new game selection
    if playerAction == "new game":
        user1 = newPlayer()
        startingItems = giveStartingItems()
        user1.inventory = startingItems

    #quit the program softly
    if playerAction.lower() == 'q':
        exit()
