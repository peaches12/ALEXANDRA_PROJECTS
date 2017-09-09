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
    for number in range(7):
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
    return new_index
def check_winner(index, XOList, XO):
    '''Checks horizontally, vertically, & diagonally to see if anyone's won yet'''
    increments = [-8, -6, -7, -1, 1, 6, 7, 8]
    for difference in increments:
        checker = ''
        for y in range(4):
            addIndex = index + increment * y 
            if 0 <= addIndex <= 48:
                checker += XOList[addIndex]
            else:
                break
            
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

write_grid(PlaceValueXO)

def someonesTurn(CC, PVXO, CTO, aWon, player, XorO):
    Column = int(input(player + ", enter Column # 1-7: "))
    if 1 <= Column <= 7:
        if CC[Column] <= 7:
            ColumnPosition = (7*(Column-1)) + ColumnCoins[Column]
            CC[Column] += 1
            New_index = switch_systems(ColumnPosition, CC, PVXO, CTO, XorO)
            write_grid(PVXO)
            aWon = check_winner(New_index, PVXO, XorO)
            if aWon == True:
                print("Horray! " + player + " won!")
            return aWon
while anyOneWon == False:
    if someonesTurn(ColumnCoins, PlaceValueXO, ColumnToRow, anyOneWon, POne, 'O') == True:
        break
    if someonesTurn(ColumnCoins, PlaceValueXO, ColumnToRow, anyOneWon, PTwo, 'X') == True:
        break

    
