minimum = 1
maximum = round(9999**(1/3))

#there are only 2 'taxicab numbers'...don't waste computer energy :)
foundYet = 0

def isthereanythingelse(primera, secunda, Question):
    for k in range(1, maximum+1):
        for y in range(1, maximum+1):
            #make sure computer understands x**3+y**3=y**3+x**3
            if (k == primera and y == secunda) or (k == secunda and y == primera):
                pass
            else:
                comparer = k**3 + y**3
                if comparer == Question:
                   print("And the winner is..." + str(comparer) + "!!!!")
                   print(str(k) + '^^3 + ' + str(y) + '^^3 = ' + str(taxicabMaybe)) 
                   return True
                
            

    
for numOne in range(1, maximum+1):
    for numTwo in range(1, maximum+1):
        taxicabMaybe = numOne**3 + numTwo**3
        
        if 1000 <= taxicabMaybe <= 9999 and foundYet < 2:
            
            if isthereanythingelse(numOne, numTwo, taxicabMaybe) == True:
    
                print(str(numOne) + '^^3 + ' + str(numTwo) + '^^3 = ' + str(taxicabMaybe))
                foundYet += 1
                
