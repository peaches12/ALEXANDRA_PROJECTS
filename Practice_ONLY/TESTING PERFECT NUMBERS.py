def is_multiple(multipleMaybe, number):
    if number%multipleMaybe == 0:
        return True
def sum_of_proper_divs(Numero):
    SUM = 0
    for MULTIPLE in range(1, int(Numero/2+1)):
        if is_multiple(MULTIPLE, Numero) == True:
           SUM = SUM + MULTIPLE
    return SUM

for y in range(100, 1000):
    if sum_of_proper_divs(y) == y:
        print("Perfect number: " + str(y))
    
