minimum = 1
maximum = 5
One = []
Two = []
for a in range(1, maximum + 1):
    for b in range(1, maximum + 1):
        Comparer = (str(a)[::-1] + str(b)[::-1])[::-1]
        print(Comparer)
        for loop in range(len(One)):
            curLOne = One[loop]
            curLTwo = Two[loop]
            TestIt = str(curLOne) + str(curLTwo)
            if Comparer != TestIt:
                One.append[a]
                Two.append[b]
print(One)
print(Two)
            
