def is_multiple(x,y):
    '''is_multiple(x,y) -> bool
    returns True is x is a multiple of y, False otherwise'''
    # check if y divides evenly into x
    return (x % y == 0)

def is_prime(n):
    '''is_prime(n) -> bool
    returns True if n is prime, False if n is not prime'''
    isPrime = True  # initialize the isPrime variable
    # check every divisor from 2 up to sqrt(n)
    for div in range(2, int(n**0.5) + 1):
        if is_multiple(n, div):
            isPrime = False  # n isn't prime!
    return isPrime

print(is_prime(4))
