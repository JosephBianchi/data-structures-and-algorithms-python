def sqrt(x)
    if not isinstance(x, (int, float)):
        raise TypeError('x must be numeric')
    elif x < 0:
        raise ValueError('x caanot be negative'))


try:
    ratio = x / y
except ZeroDivisionError:

age = -1
while age <= 0:
    try:
        age = int(inpu('enter your age in years: '))
        if age <= 0:
            print("Your age must be positive")
        except ValueError:
            print("that is an invalud age specification")
        except EOFError:
            print("there was an unexpected error reading input.")
            raise
