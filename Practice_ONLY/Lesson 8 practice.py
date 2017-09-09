'''FILES & TRIALS: INFO from EXTERNAL sources'''
def word_lengh_counter():
    inFile = open('text_test.txt','r')  # open file
    fileString = inFile.read()   # read entire file into a string
    inFile.close()   # we're done with the file, so we can close it now
    wordList = fileString.split()
    lengths = []
    for words in wordList:
        lengths.append(len(words))

    for x in range(1, 14):
        print("Number of " + str(x) + '-letter words: ' + str(lengths.count(x)))

   
def alphabetize_everything():
    inFile = open('text_test.txt','r')  # open file
    fileString = inFile.read()   # read entire file into a string
    inFile.close()   # we're done with the file, so we can close it now
    wordList = fileString.split()
    wordList.sort()
    comparer = ''
    for word in wordList:
        if word != comparer:
           print(word)
        comparer = word
 

