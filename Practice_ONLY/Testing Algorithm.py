number = int(input("What factorial do you want to find?"))
product = 1
for k in range(number):
    product = product * (k+1)
    print(str(product))
print(str(product))
