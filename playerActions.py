def pickupItem():
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


def playerMove(playerAction, user1):
    # player movement logic
    if playerAction in user1.location.exits:
        user1.location = user1.location.exits[playerAction]
        print("You go {} and find yourself in a ".format(playerAction) + user1.location.roomName)
        print(user1.location.description)
        randomEncounter()
    else:
        print("Unable to move in that direction\n")

    return user1
