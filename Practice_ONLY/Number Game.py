# Python Class 1548
# Lesson 6 Problem 6 part (b)
# Author: peaches1210 (202437)
import random, sys
def backgammon_roll():
    dieOne = random.randrange(1, 6)
    dieTwo = random.randrange(1, 6)
    if dieOne == dieTwo:
        return 2*(dieOne+dieTwo)
    else:
        return dieOne + dieTwo

imdone = False

playerOne = 0
playerTwo = 0

OneScore = 0
TwoScore = 0

while imdone != True:
    print("StartPoints: playerOne: " + str(playerOne) + "; playerTwo: " + str(playerTwo) + '\n')
    winOne = False
    winTwo = False
    while winOne == False and winTwo == False:
        playPoints = backgammon_roll()
        print("Player one rolled: " + str(playPoints))
        playerOne += playPoints
        print("The score is: PlayerOne: " + str(playerOne) + " points; PlayerTwo: " + str(playerTwo))
    
        if playerOne > 100:
            winOne == True
            print("Player 1 wins!")
            playerOne = 10
            playerTwo = 0
            OneScore += 1
            break
        
        playPoints = backgammon_roll()
        print("Player two rolled: " + str(playPoints))
        playerTwo += playPoints
        print("The score is: PlayerOne: " + str(playerOne) + " points; PlayerTwo: " + str(playerTwo))
    
        if playerTwo > 100:
            winTwo == True
            print("Player 2 wins!")
            playerTwo = 10
            playerOne = 0
            TwoScore += 1
            break
    print('')
    print("Current Score: PlayerOne--" + str(OneScore) + "; PlayerTwo--" + str(TwoScore))
    if OneScore > TwoScore:
        print("\nONE IS WINNING!")
    elif TwoScore > OneScore:
        print("\nTWO IS WINNING!")
    else:
        print("\nYOU'RE TIED!") 
    print('')    
    Quit = input('''I know this game is boring.
If you want to quit, press 'y', 'Y', or 'YES'
If not, type something else: ''')
    print('')
    if Quit == 'y':
        imdone == True
        print("Thanks for playing anyway.") 
        sys.exit()
    
        
    
#
