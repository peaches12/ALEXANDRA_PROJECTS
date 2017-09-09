#this program will try to guess a 4-6 letter-number password
import sys, time
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
current = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
in_da_making = []

counter = 0

password = input("String using letters a-j plz: ")
for x in range(9):
    for k in range(len(current)):
        firstLetter = current[k]
        for m in range(len(letters)):
            addit = letters[m]
            appendit = firstLetter + addit
            counter = counter + 1
            if appendit == password:
                print("We have it! It took " + str(counter) + " tries, but we have it anyway!")
                sys.exit()
            in_da_making.append(appendit)
    
    current = in_da_making
    in_da_making = []

    

    
    
    
