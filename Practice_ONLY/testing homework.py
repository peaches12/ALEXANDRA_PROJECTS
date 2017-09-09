def how_many_times(sentance, letra):
    index = 0
    occurances = 0
    while index != -1:
        index = sentance.find(letra, index+1)
        occurances += 1 
    return occurances
def most_common_letter(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    string = string.lower()
    print(string)
    maximumNumber = 0
    maxLetter = ''
    for letter in alphabet:
        if how_many_times(string, letter) > maximumNumber:
            maximumNumber = how_many_times(string, letter)
            maxLetter = letter
    return maxLetter

# example
excerpt = '''
"My dear fellow," said Sherlock Holmes as we sat on either side of the fire in his lodgings at 
Baker Street, "life is infinitely stranger than anything which the mind of man could invent. We 
would not dare to conceive the things which are really mere commonplaces of existence."
'''

# by Sir Arthur Conan Doyle
print("Occuring Letter: " + most_common_letter(excerpt))
