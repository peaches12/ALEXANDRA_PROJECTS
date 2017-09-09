import math
ColumnCoins = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0}
NumberXO = {}
orderOrder = []
for columns in range(6, -1, -1):
    for rows in range(7):
        orderOrder.append(columns + rows * 7)
print(orderOrder)
def write_grid(XOList):
    '''prints the current playing grid'''
    print(XOList)
    for row in range(0, 49, 7):
        for XOspace in range(row, row+7):
            print(str(XOList[XOspace]) + ' ', end='')
        print('\n')

def XO_Turn(INPUT, listOne, listTwo, listThree, XorO):
    '''switches from column order to row order'''
    listOne[INPUT] += 1
    row_position = INPUT * 7 + listOne[INPUT]
    print(row_position) 
    writingPlace = listThree.index(row_position)
    listTwo[writingPlace] = XorO
    return listTwo

def SomeonesTurn(CC, NXO, OO, XO):
    '''accepts input from a player'''
    Oinput = int(input("Player " + str(XO) + ", please enter a column number 1-5: "))
    if CC[Oinput] < 7:
        grid_list = XO_Turn(Oinput, CC, NXO, OO, XO)
        write_grid(grid_list)
    else:
        print("Sorry, that row's already full. Try again.")

def check_winner(NXO, XorO):
    '''checks horizonally, vertically, & diagonally if there's 4-in-a-row'''
    #HORIZONTALLY
    number_checks = int(math.sqrt(len(NumberXO))-3) #how many sets of 4 do we need to check in a row/column?
    for row_checks in range(0, 49, 7):              #the beginning of each row
        for each_row in range(number_checks):       #we need to check 2 lists/row
            firstDot = row_checks+each_row          #find the first X or O in the row we're checking
            OXstring = ''                           #reset the test string
            for OX in range(4):
                OXstring += NXO[firstDot+OX]
            print(OXstring)
            if OXstring == XorO*4:                  #if the string is all Xs or all Os
                return True
    #VERTICALLY
    for column_checks in range(0, 5):               #beginning of each column
        for each_column in range(number_checks):
            starter = column_checks + each_column*5
            checker = ''
            for XO in range(4):
                checker += NXO[starter+XO*5]
            if checker == XorO * 4:
                return True
    return False
    #vertically
    
    return False
#we haven't put any Xs or Os in yet
for num in range(49):
    NumberXO[num] = '*'


win = False
while win == False:
    SomeonesTurn(ColumnCoins, NumberXO, orderOrder, 'O')
    print(check_winner(NumberXO, 'O'))
    SomeonesTurn(ColumnCoins, NumberXO, orderOrder, 'X')
    print(check_winner(NumberXO, 'X'))
    
    
     
