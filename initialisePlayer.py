from classStructure import player

# create a new player object when called from the main loop
def newPlayer():
    userName = input("What is your name?\n")

    user1 = player(userName, 'entrance')

    print("Welcome to your Adventure, " + user1.name + "!")

    return user1
