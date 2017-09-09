def two_word_split(palabra):
    wordOne = ''
    wordTwo = ''
    wordList = []
    if len(palabra) % 2 == 1:
        lastLetter = palabra[len(palabra)-1]
    else:
        lastLetter = ''
    for letter in range(len(palabra)//2):
        wordOne += palabra[letter*2]
        wordTwo += palabra[letter*2+1]
    wordOne += lastLetter
    wordList.append(wordOne)
    wordList.append(wordTwo)
    return wordList

def Insert_word(One, Two):
    partOne = One[0]
    partThree = One[1:len(One)]
    return (str(partOne) + str(Two) + str(partThree))


def Caesar_shift(word, shift):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    disguiseWord = ''
    for letter in word:
        crudeIndex = letters.find(letter)
        if crudeIndex + shift < 26:
            newIndex = crudeIndex + shift
        else:
            newIndex = (crudeIndex+shift) % 26
        disguiseWord += letters[newIndex]
    return disguiseWord 


ended = False
while ended == False:
    translateSentance = input("Enter a sentance please: ")
    splitSentance = translateSentance.split()
    disguisedSentance = ''
    for normalword in splitSentance:
        CeaserIt = Caesar_shift(normalword, len(normalword))
        
        ListTwoWords = two_word_split(CeaserIt)
        
        FinalProduct = Insert_word(ListTwoWords[0], ListTwoWords[1])
        
        disguisedSentance += str(FinalProduct) + ' '
    print(disguisedSentance)
    print("See program 'Alussian to English' to translate back into readable language")
    QuitOrNot = input("Would you like to quit? y/n: ")
    if QuitOrNot == 'y' or 'Y' or 'yes':
        ended = True
    

