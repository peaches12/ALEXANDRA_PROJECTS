import random
''' 1  2  3   4  5 6
    7  8  9  10 11 12
    13 14 15 16 17 18
    19 20 21 22 23 24
    25 26 27 28 29 30
    31 32 33 34 35 36'''
#dictionaries, lists, & constant variables
playingSpots = {}
alphabet = 'abcdefghijklmnopqrstuvwxyz'
points = 0

#functions
def draw_grid(PS):
    '''draws the letter grid'''
    Values = list(PS.values())
    print('')
    for row in range(0, 16, 4):
        for individ in range(4):
            print(Values[row+individ] + ' ', end='')
        print('')

def is_word_in_grid(palabra, PlaySpot):
    '''determines if the word is 'in' the grid'''
    #first letter indexes (all of them)
    Numbers = list(PlaySpot.keys())
    Letters = list(PlaySpot.values())
    firstLetters = first_letter_indexes(palabra, PlaySpot)
    print("How many times does " + str(palabra[0]) + " occur?: " + str(firstLetters) + " times.")
    #if the first letter isn't even in the grid
    if len(firstLetters) == 0:
        return False
    addIt = [-7, -6, -5, -1, 1, 5, 6, 7]
    for y in range(1, len(palabra)):              #don't look for the first letter
        Loopletter = palabra[y]                        #letter we're checking for
        newIndexList = []                              #the new indexes for the next letter
        for index in firstLetters:                     #check around each letter for the consecutive letter
            for addend in addIt:                       #do this for all the addends in AddIt
                newOne = index + addend                #find index of value above/below/diagonally across current value
                if newOne in Numbers:                  #if the index is actually in the list of approved values
                    if PlaySpot[newOne] == Loopletter:  #if the index corresponds w/ the correct letter
                        if newOne not in newIndexList: #no index repeats in the list
                            newIndexList.append(newOne)#append newOne
        firstLetters = newIndexList        
        print("How many times does " + str(Loopletter) + " occur?: " + str(firstLetters) + " times.")
        if len(newIndexList) == 0:                     #if the next letter isn't 1 unit away from the current one 
            return False                               #the word isn't in the grid
    #if the word occurs at least once
    return True                                             
        
                                       
def first_letter_indexes(mon, PS):
    '''find how many times the 1st letter shows up in the grid'''
    starter = mon[0]
    GridNumbers = list(PS.keys())
    GridLetters = ''.join(list(PS.values()))
    
    IndexResult = -1
    LetterIndexes = []

    while True:
        IndexResult = GridLetters.find(starter,IndexResult+1)
        if IndexResult == -1:                               #if there aren't any more 'starters' left
            break
        appendPositon = GridNumbers[IndexResult]            #find the corresponding number in GridNumbers 
        LetterIndexes.append(appendPositon)
    return LetterIndexes
    
#pick random letters for the playing grid
for row in range(8, 27, 6):
    for number in range(4):
        key = row+number
        randNumb = random.randint(0, 25)
        value = alphabet[randNumb]
        playingSpots[key] = value

#playing the game
while points < 51:
    draw_grid(playingSpots)
    word = input("Enter a word with more than 2 letters that you find in the grid: ")
    if len(word) > 2:
        print(is_word_in_grid(word, playingSpots)) 
    else:
        print("The word must be at least 3 letters.") 

