#Lists & Dictionaries
ColumnCoins = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0}
PlaceValueXO = {}
ColumnToRow = []
#FUNCTIONS
def write_grid(XsANDOs):
    for row in range(7):
        for individual in range(7):
            print(XsANDOs[(row*7) + individual] + ' ', end='')
        print('\n') 
#fill up ColumnToRow
for rowStart in range(6, -1, -1):
    for placeHolder in range(7):
        ColumnToRow.append(rowStart + 7*placeHolder)
#fill up PlaceValueXO
for XO in range(49):
    PlaceValueXO[XO] = '*'
#Collect Input
Column = int(input("Enter Column # 1-7: "))
if 1 <= Column <= 7:
    ColumnPosition = (7*(Column-1)) + ColumnCoins[Column]
    ColumnCoins[Column] += 1
    new_index = ColumnToRow.index(ColumnPosition)
    PlaceValueXO[new_index] = 'O'
    print(PlaceValueXO)
    write_grid(PlaceValueXO) 
    
