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
    print(Values)
    for row in range(0, 16, 4):
        for individ in range(4):
            print(Values[row+individ] + ' ', end='')
        print('')

def is_word_in_grid(palabra, PS):
    starter = palabra[0]
    GridNumbers = list(PS.keys())
    GridLetters = list(PS.values())
    
#pick random letters for the playing grid
for row in range(8, 27, 6):
    for number in range(4):
        key = row+number
        randNumb = random.randint(0, 25)
        value = alphabet[randNumb]
        playingSpots[key] = value

while points > 51:
    word = input("Enter a word with more than 2 letters that you find in the grid: ")
    if len(word) > 2:
        is_word_in_grid(word, playingSpots) 
    else:
        print("The word must be at least 3 letters.") 
