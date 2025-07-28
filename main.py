from initialisePlayer import *
playerAction=''

while playerAction.lower() != 'q':
    playerAction = input("What would you like to do?\n").lower()

    if playerAction == "new game":
        newPlayer()
