#returns a NUMBER

message = input("Enter a message: ")
message = list(message)
newMessage = ''
smallCharacters = 'abcdefghijklmnopqrstuvwxyz'
bigCharacters = smallCharacters.upper()
#result is supposed to be 'secret' shifted by 1 letter--> 'tfdsfu'
for character in message:
    
    if character in smallCharacters or character in bigCharacters: #is the next character a
        #make a note if our character is upper/lowercase
        if character.isupper() == True:
            upper = True
        else:
            upper = False
        character = character.lower()           #lowercase it to avoid errors
        index = smallCharacters.find(character) #find current index
        
        if index + 13 < 26:                     #if there's no risk of going past index 25
            newLetter = smallCharacters[index+13]
        else:                                   #bring the new index back to 0-25 range
            newLetter = smallCharacters[(index+13)%26]
        #make sure you keep capitalization
        if upper == True:
            newLetter = newLetter.upper()
    else:                                       #non-letter characters don't change
        newLetter = character
    
    newMessage += str(newLetter)                #add the new letter to the message

#print it (duh)
print(newMessage)
