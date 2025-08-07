import random

def pickupItem(itemChoice, user1):
    '''if itemChoice in user1.location.items:
        removedItem = user1.location.items.key()
        removedDescription = user1.location.items.value()

        print(removedItem, removedDescription)
        user1.location.items.remove(removedItem)
        createdItem = items()
    else:
        print("No item by that name: " + itemChoice)

    return user1'''
    pass

def equipWeapon(user1):
    weaponChange = False
    weaponSelect = input("equip which weapon?\n").lower()
    for i in range(0,len(user1.inventory)):
        if weaponSelect == user1.inventory[i].name.lower():
            weaponSelect = user1.inventory[i]
            swapWeapon(weaponSelect, user1)
            break

    return user1

def swapWeapon(selectedWeapon, user1):
    if selectedWeapon.isWeapon:
        user1.playerHeldWeapon = selectedWeapon
        user1.holdingWeapon = True
        user1.inventory.remove(selectedWeapon)
        print("you have equiped: " + user1.playerHeldWeapon.name)
    else:
        print("That is not a weapon")

    return user1

def viewStats(user1):
    print("Player Name: " + user1.name)
    print("HP: " + str(user1.playerHP))
    print("Inventory:")
    for i in range(0, len(user1.inventory)):
        print("    " + user1.inventory[i].name + ": " + user1.inventory[i].description, user1.inventory[i].isWeapon)
    if user1.holdingWeapon:
        print("Equipped Weapon: " + user1.playerHeldWeapon.name, user1.playerHeldWeapon.description)
    else:
        print("Equipped Weapon: None")

    return user1

def randomEncounter(user1):
    # Create a chance of a random encounter occurring
    encounterChance = random.randint(0, 100)

    if user1.location.enemyRoom:
        if 0 < encounterChance < 30:
            print("you find an empty room")
        elif 30 < encounterChance < 90:
            print("You find  goblin")
        else:
            print("You encounter the king goblin")
    return user1

def playerMove(playerAction, user1):
    # player movement logic
    if playerAction in user1.location.exits:
        user1.location = user1.location.exits[playerAction]
        print("You go {} and find yourself in a ".format(playerAction) + user1.location.roomName)
        print(user1.location.description)
        for key in (user1.location.exits.keys()):
            print("There is an exit: " + key)
        randomEncounter(user1)
    else:
        print("Unable to move in that direction\n")

    return user1
