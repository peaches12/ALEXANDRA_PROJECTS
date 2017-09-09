#THIS PROGRAM FINDS THE SUM OF THE 1st N FIBONACCI NUMBERS
find_number = int(input("What is n?"))
counter = 1
cur_num = 1
add_it = 0
SUM = 0
while counter <= find_number:
    SUM = cur_num + add_it
    add_it = cur_num
    cur_num = add_it + cur_num
    counter = counter + 1
    
    print(SUM) 
