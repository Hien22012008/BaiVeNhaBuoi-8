n = int(input('Input n:'))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(f'First {n} prime(s): ')

result = 0

for i in range(1, n + 1):
    result += 1
    while is_prime(result) != True:
        result += 1
    print(result)
