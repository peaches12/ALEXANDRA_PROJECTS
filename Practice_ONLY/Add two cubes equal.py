import time
smallest_addit = 1
largest_addit = round(9999 ** (1/3))
options_list = []
for x in range(smallest_addit, largest_addit + 1):
    current_starter = x
    for y in range(smallest_addit, largest_addit + 1):
        current_secondNumber = y
        listAppend = x ** 3 + y ** 3
        #if listAppend is a 4-digit number
        if 999<listAppend<9999:
            options_list.append(listAppend)   #append the lastest 3-cube to the list
            for a in range(len(options_list) - 1):
                if listAppend == options_list[a]:
                    print("We have it!" + str(a))
                    print("The number is: " + str(listAppend))
            




                        

