from initialisePlayer import *
playerAction=''

#This aims to be the main game loop
while playerAction.lower() != 'q':
    playerAction = input("What would you like to do?\n").lower()

    if playerAction == "new game":
        newPlayer()
