num = float(input('Input number:'))

def is_int(n):
    if n == round(n):
        return True
    else:
        return False

if is_int(num):
    print(num,'is an integer')
else:
    print(num,'is not an integer')