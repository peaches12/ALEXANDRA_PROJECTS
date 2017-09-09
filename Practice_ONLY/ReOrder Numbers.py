from random import randint
#strings, lists, and inputs oh my
finalproduct = ''
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers_o = []
alphabetical = []

digits = int(input("Enter # of digits 1-26: "))             #self-explanatory

originalNumber = randint(10**(digits-1), 10**digits)        #manipulating powers
print("Original: " + str(originalNumber))

order = input("Using letters a through " + letters[digits-1] + ", write the order " + str(originalNumber) + " needs to be mixed. ")

changeLetters = list(order)                                 #list everything

#we need a gramatically correct baseline
for k in range(digits):
    alphabetical.append(letters[k])

#we could've used list(), but I'm trying to practice arithmetic :)
for y in range(digits-1, -1, -1):
    currentNumber = originalNumber//10**y
    originalNumber = originalNumber - (currentNumber * 10**y)
    numbers_o.append(currentNumber)

for loop in range(len(numbers_o)):
    correctorderL = changeLetters[loop]             #find the first represented letter
    misplacedIndex = alphabetical.index(correctorderL)    #find the index of variable above
    appendIt = numbers_o[misplacedIndex]            #find the append digit
    finalproduct = finalproduct + str(appendIt)         #add the digit on


print("Mixup: " + str(order))
print("New: " + str(finalproduct))
print("Enjoy your new number!")

    
