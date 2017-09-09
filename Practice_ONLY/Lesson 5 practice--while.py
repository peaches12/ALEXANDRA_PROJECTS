#this program finds the longest Collatz sequence w/ first term a <1000
def collatz_number(NUMBER):
    if NUMBER%2 == 0:
        return int(NUMBER/2) 
    else:
        return int(NUMBER*3+1)
def collatz_lengh(number):
    print("Works")
    lengh = 0
    while number != 1:
        number = number + collatz_number(number)
        lengh += 1
    return lengh

comparer = 0

for loop in range(2, 1000):
    if collatz_lengh(loop) > comparer:
        comparer = collatz_lengh(loop)


    
    
