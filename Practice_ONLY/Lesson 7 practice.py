def longest_word_v1(string):
    longest_word_v2(string):
    '''input-->a string
        output-->max word lengh'''
    string = string.split()
    comparer = 0
    longWord = ''
    for word in string:
        currentLengh = len(word)
        if currentLengh > comparer:
            comparer = currentLengh            
    return comparer

def longest_word_v2(string):
    '''input-->a string
        output-->max word lengh'''
    string = string.split()         #split string into words
    wordList = []                   #empty list
    for word in string:
        wordList.append(len(word))  #append word lengh
    return max(wordList)
    
def picky_digit_v1():
    '''all specific 2-digit numbers w/o repeating digits'''
    digits = [2, 3, 5, 7]
    specialNumbers = []
    for firstNumber in digits:
        for secondNumber in digits:
            if firstNumber != secondNumber:
                specialNumbers.append(str(firstNumber) + str(secondNumber))
    return specialNumbers

def picky_digit_v2():
    '''includes repeats (77, 55)'''
    digits = [2, 3, 5, 7]
    specialNumbers = []
    for tens in digits:
        for ones in digits:
            specialNumbers.append(str(tens*10 + ones))
    return specialNumbers





