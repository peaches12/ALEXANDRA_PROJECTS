import random, sys
''' 1  2  3   4  5 6
    7  8  9  10 11 12
    13 14 15 16 17 18
    19 20 21 22 23 24
    25 26 27 28 29 30
    31 32 33 34 35 36'''
#dictionaries, lists, & constant variables
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
    for y in range(1, len(palabra)):                   #ignore the first letter
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
def pick_grid():
    PS = {}
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for row in range(8, 27, 6):
        for number in range(4):
            key = row+number
            randNumb = random.randint(0, 25)
            value = alphabet[randNumb]
            PS[key] = value
    return PS

#finding out if the word is in word_file
def real_word(palabra, cada_palabra):                   
    for WoRd in cada_palabra:                              #check EVERY word...I know it's inefficient, but it's the rule.
        WoRd = WoRd.strip()                                #get rid of the space
        if palabra == WoRd:
            return True
    return False

#how many points is this word worth?
def find_point_number(mon):
    '''finds how many points the valid word is worth'''
    lengh = len(mon)        
    lenghValue = {3:1, 4:2, 5:3, 6:5, 7:6, 8:8, 9:10}      #I'm to lazy to type out 1000 elif statements
    #anticipate errors
    while True:
        try:
            puntas = lenghValue[lengh]
            return puntas
        except ValueError:                                 #the word is longer than 9 letters
            return 14

        
#opening/reading the word file
word_file = open('Words.txt', 'r')
each_word = list(readlines(word_file))
#playing the game
while points < 100:
    playingSpots = pick_grid()                              #make a new grid...in case there ain't no words 
    draw_grid(playingSpots)                                 #draw the NEW grid :)
    word = input("Type 'Quit' to end game. Type 'N/A' for another word-grid. Enter a word with more than 2 letters that you find in the grid if you want to play: ")
    if word == 'N/A':                                       #if the person wants another grid
        continue
    elif word == 'Quit':                                    #if the person is B.O.R.E.D.
        print("Thanks for playing!")
        print("You've earned: " + str(points) + " points.")
        sys.exit()                                          #easiest way to shut-down fast
    if len(word) > 2:                                       #is the word longer than 3 letters?
        if real_word(word, each_word) == True:              #if the word is in the word list
            IN_GRID = is_word_in_grid(word, playingSpots)   #check to see if the word is in the grid
            if IN_GRID == True:                             #if the 3 above conditions are satisfied...
                points += find_point_number(word)           #calculate # of points it contributes & add to total
            else:
                print("Sorry, the word isn't in the grid.") #error message
        else:
            print("That isn't a real word. Try again.")     #try again 
    else:
        print("The word must be at least 3 letters.")       #how many errors can there be again?
        
#a friendly final message
print("Thanks for playing!")
sys.exit()

