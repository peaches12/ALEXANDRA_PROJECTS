#cherry pick vowels from word

def pick_vowels(word):
    unorderedVowels = ''
    vowelsConsonants = []
    for letter in word:
        if letter in 'aeiouy':
            unorderedVowels += letter
            word = word.replace(letter, '', 1)
    vowelsConsonants.append(unorderedVowels)
    vowelsConsonants.append(word)
    return vowelsConsonants

#put vowels in alphabetical order

def alphabetical_vowels(messyVowels):
    alphieVowels = ''
    VOWELS = 'aeiouy'
    for vowel in VOWELS:
        for letra in messyVowels:
            if letra == vowel:
                alphieVowels += vowel
    return alphieVowels

#translate a simple sentance into Alussian

needATranslator = input("Enter a sentance: ")

def alussian_translate(sentance):
    separate_words = needATranslator.split()
    translatedSentance = ''
    for englishWord in separate_words:
        
        mixedUp = pick_vowels(englishWord)[0]   #the vowels before they're alphabetized
        ordered = alphabetical_vowels(mixedUp)  #the vowels in aeiouy order
        consonants = pick_vowels(englishWord)[1]#the consonants...in order
        
        separateCats = str(ordered) + str(consonants)#mush the vowels & the consonants
        if len(separateCats) > 1:                         #if it isn't a one-letter word
            if len(consonants) < len(ordered):            #if there are more vowels than consonants
                separateCats += 'ay'                      #add an 'ay'
            else:
                separateCats += separateCats[1] + separateCats[0]  #just add the second letter twice tot he end
        else:
            separateCats += 'e'                      #only options are 'ie' and 'ae'
        translatedSentance += separateCats + ' '     #add word to the sentance
        
    return translatedSentance

print(alussian_translate(needATranslator))
