def pickOut_word(mot, lengh):

    listaPalabra = []
    firstWord = mot[0] + mot[(lengh//2+1):(lengh)]
    secondWord = mot[1:(lengh//2) + 1]

    listaPalabra.append(firstWord)
    listaPalabra.append(secondWord)
    return listaPalabra

def Ceasar_reshift(word, LeNgH):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    disguiseWord = ''
    for letter in word:
        crudeIndex = letters.find(letter)
        if crudeIndex - LeNgH < 0:
            newIndex = crudeIndex-LeNgH + 26
        else:
            newIndex = crudeIndex - LeNgH 
        disguiseWord += letters[newIndex]
    return disguiseWord

def pieceWordTogether(firstSection, secondSection):
    finalWord = ''
    if len(firstSection) != len(secondSection):
        lastLetter = firstSection[-1]
    else:
        lastLetter = ''
    for letter in range(len(secondSection)):
        finalWord += firstSection[letter]
        finalWord += secondSection[letter]
    finalWord += lastLetter
    return finalWord

endIt = False
while endIt == False:
    AlussianSentance = input("Enter a sentance please: ")
    splitSentance = AlussianSentance.split()
    regularSentance = ''
    
    for oddWord in splitSentance:
        EnglishLetters = Ceasar_reshift(oddWord, len(oddWord))
        wordList = pickOut_word(EnglishLetters, len(EnglishLetters))
        wordOne = wordList[0]
        wordTwo = wordList[1]
        newWord = pieceWordTogether(wordOne, wordTwo)
        regularSentance += str(newWord) + ' '
        
    print(regularSentance)
    
    QuitOrNot = input("Would you like to quit? y/n: ")
    if QuitOrNot == 'y' or 'Y' or 'yes':
        ended = True


