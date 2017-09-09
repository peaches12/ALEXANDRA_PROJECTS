import time
def is_prime(number):
    primeMaybe = True
    for loop in range(2, int(number/2)+1):
        if number%loop == 0:
            primeMaybe = False
    if number == 2:
        primeMaybe == True
        
    return primeMaybe

total_primes = 0
SUM = 0
for k in range(2, 545):
    print(str(k) + " prime: " + str(is_prime(k)))
    if is_prime(k) == True:
        total_primes += 1
        SUM = SUM + k
print("Total primes: " + str(total_primes))
print("Sum of primes: " + str(SUM))
