from classStructure import player, weapon, item

# create a new player object when called from the main loop
def newPlayer():
    userName = input("What is your name?\n")

    user1 = player(userName, 'entrance')

    print("Welcome to your Adventure, " + user1.name + "!")

    return user1

def giveStartingItems():
    sword = weapon("Sword","A small basic sword with no flare")
    sword.isWeapon = True
    sword.minDamage = 1
    sword.maxDamage = 3

    rope = item("Rope","Some rope that may come in handy later")
    linen = item("Linen","A length of linen cloth")

    startingItems = [sword, rope, linen]
    return startingItems

def equipWeapon(selectedWeapon, user1):
    if selectedWeapon.isWeapon:
        user1.playerHeldWeapon = selectedWeapon
        user1.holdingWeapon = True
        user1.inventory.remove(selectedWeapon)
        print("you have equiped: " + user1.playerHeldWeapon.name)
    else:
        print("That is not a weapon")

    return user1
