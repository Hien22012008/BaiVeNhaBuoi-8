n = int(input('Input n:'))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if is_prime(n) == True:
    print(n,'is a prime')    
else:
    print(n,'is not a prime')