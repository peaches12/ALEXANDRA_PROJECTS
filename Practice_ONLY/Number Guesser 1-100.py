import random


guessed = False
NumberOfGuesses = 0

computerNumber = random.randrange(1, 101)

while guessed == False: 
    GuessIt = int(input("Number guess: "))
    NumberOfGuesses += 1
    if GuessIt > computerNumber:
        print("Sorry, " + str(GuessIt) + " is too high.")
    elif GuessIt < computerNumber:
        print("Sorry, " + str(GuessIt) + " is too low.")
    else:
        print("CONGRATULATIONS! " + str(GuessIt) + " is my number!")
        if NumberOfGuesses > 10:
            print("No offense, but you're a pretty bad guesser.")
        elif 5 < NumberOfGuesses <= 10:
            print("Eh. I guess you're an average guesser.")
        else:
            print("WOW! You must be a bit-reader or something. Or maybe today's a lucky day?")
        print("Cuz you took " + str(NumberOfGuesses) + " to get it right.")
        guessed == True 
        break
