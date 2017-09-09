# Python Class 1548
# Lesson 12 Problem 1
# Author: peaches1210 (202437)

#Connect4#

#Lists & Dictionaries & variables

ColumnCoins = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0}
PlaceValueXO = {}
ColumnToRow = []
anyOneWon = False
#FUNCTIONS
def write_grid(XsANDOs):
    '''input: list of XO*'s
    output: grid of Xs and Os'''
    print('')
    #the 1-7 at the top
    for number in range(1, 8):
        print(str(number) + ' ', end='')
    print('\n')
    #the actual Xs, Os, and *s
    for row in range(7):
        for individual in range(7):
            print(XsANDOs[(row*7) + individual] + ' ', end='')
        print('\n')
        
def switch_systems(CoPo, CC, PVXO, CTR, XorO):
    '''input: ColumnPosition, all 3 lists/dictionaries, and if it's
    X or O
       output: PlaceValueXO, altered'''
    new_index = CTR.index(CoPo)
    PVXO[new_index] = XorO
    return PVXO
def check_winner(XOList, XO):
    '''Checks horizontally, vertically, & diagonally to see if anyone's won yet'''
    #HORIZONTALLY
    for row in range(7):
        firstValue = row * 7
        for section in range(4):
            starter = firstValue + section
            XOSection = ''
            for index in range(starter, starter+4):
                XOSection += XOList[index]
            if XOSection == XO*4:
                return True
    #VERTICALLY
    for StartColumn in range(7):
        for section in range(4):
            starter = StartColumn + section * 7
            Number = ''
            XOSection = ''
            for index in range(starter, starter + 28, 7):
                Number += str(index) + ' '
                XOSection += XOList[index]

            if XOSection == XO*4:    
                return True
    #DIAGONALLY
    #left to right, moving down
    for rowStarter in range(0, 28, 7):
        for diagStart in range(4):
            XODiag = ''
            TopNum = rowStarter + diagStart
            for individ in range(0, 32, 8):
                XODiag += XOList[individ + TopNum]
               
            if XODiag == XO * 4:
                return True
    #right to left, moving up
    for rowStarter in range(6, 34, 7):
        for diagStart in range(4):
            XODiag = ''
            TopNum = rowStarter - diagStart
            for individ in range(0, 24, 6):
                XODiag += XOList[individ + TopNum]
                Number += str(individ + TopNum) + ' '
            if XODiag == XO * 4:
                return True        
            
    return False
#fill up ColumnToRow
for rowStart in range(6, -1, -1):
    for placeHolder in range(7):
        ColumnToRow.append(rowStart + 7*placeHolder)
#fill up PlaceValueXO
for XO in range(49):
    PlaceValueXO[XO] = '*'
#Collect Input
POne = input("O, what is your name? ")
PTwo = input("X, what is your name? ")

players = []
players.append(POne)
players.append(PTwo)

write_grid(PlaceValueXO)

turns = 0
XO = ['X', 'O'] 
def someonesTurn(CC, PVXO, CTO, aWon, player, XorO):
    '''input: all the lists, name of player, & if they're X or O
    output: True if player won'''
    Column = int(input(player + ", enter Column # 1-7: "))
    if 1 <= Column <= 7:
        if CC[Column] <= 7:
            ColumnPosition = (7*(Column-1)) + ColumnCoins[Column]
            CC[Column] += 1
            PVXO = switch_systems(ColumnPosition, CC, PVXO, CTO, XorO)
            write_grid(PVXO)
            aWon = check_winner(PlaceValueXO, XorO)
            if aWon == True:
                print("Horray! " + player + " won!")
            return aWon
while anyOneWon == False:
    for y in range(2):
        if turns > 48:
            print("The board is full. No one won.") 
            break
        turns += 1
        if someonesTurn(ColumnCoins, PlaceValueXO, ColumnToRow, anyOneWon, players[y], XO[y]) == True:
            break
    

    

#
