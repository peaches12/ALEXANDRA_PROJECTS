#Lists & Dictionaries & variables
ColumnCoins = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0}
PlaceValueXO = {}
ColumnToRow = []
anyOneWon = False
#FUNCTIONS
def write_grid(XsANDOs):
    '''input: list of XO*'s
    output: grid of Xs and Os'''
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
            Number = ''
            XOSection = ''
            for index in range(starter, starter+4):
                XOSection += XOList[index]
                Number += str(index)
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
    def diagonally(RSsmall, RSbig, IDVbig, IDVincrement):

        for rowStarter in range(RSsmall, RSbig, 7): #the top 4 edge columns
            for diagStart in range(4):              #7x7 square, four 4 diagonals
                XODiag = ''                         #initialize the current *OX string
                TopNum = rowStarter + diagStart     #the top index of the diagonal (smallest one)
                for individ in range(0, IDVbig, IDVincrement): #increment 8 for left-right, increment 6 for right-left
                    XODiag += XOList[individ + TopNum] 
                if XODiag == XO * 4:                #just Xs or just Os
                    return True

    diagonally(0, 28, 32, 8)
    diagonally(6, 34, 24, 6)      
            
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
while anyOneWon == False:
    Column = int(input(POne + ", enter Column # 1-7: "))
    #Write grid, determine if anyone won yet
    if 1 <= Column <= 7:
        if ColumnCoins[Column] <= 7:
            ColumnPosition = (7*(Column-1)) + ColumnCoins[Column]
            ColumnCoins[Column] += 1
            PlaceValueXO = switch_systems(ColumnPosition, ColumnCoins, PlaceValueXO, ColumnToRow, 'O')
            write_grid(PlaceValueXO)
            anyOneWon = check_winner(PlaceValueXO, 'O')
            if anyOneWon == True:
                print("Horray! " + POne + " won!")
                break

    Column = int(input(PTwo + ", enter Column # 1-7: "))
    if 1 <= Column <= 7:
        if ColumnCoins[Column] <= 7:
            ColumnPosition = (7*(Column-1)) + ColumnCoins[Column]
            ColumnCoins[Column] += 1
            PlaceValueXO = switch_systems(ColumnPosition, ColumnCoins, PlaceValueXO, ColumnToRow, 'X')
            write_grid(PlaceValueXO)
            anyOneWon = check_winner(PlaceValueXO, 'X')
            if anyOneWon == True:
                print("Horray! " + PTwo + " won!")
                break

    
