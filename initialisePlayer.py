from classesStructure import player
global user1

def newPlayer():
    global user1
    userName = input("What is your name?\n")

    user1 = player(userName, 'entrance')

    print("Welcome to your Adventure, " + user1.name + "!")

    return user1.name, user1.location
