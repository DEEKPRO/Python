import math
num = int(input("Enter a number: "))

def is_perfect_square(x):
    s = int(math.sqrt(x))
    return s * s == x

def is_fibonacci(n):
    return is_perfect_square(5*n*n + 4) or is_perfect_square(5*n*n - 4)

def closest_fibonacci(n):
    if n < 0:
        return None
    lower = n
    upper = n
    while True:
        if lower >= 0 and is_fibonacci(lower):
            return lower
        if is_fibonacci(upper):
            return upper
        lower -= 1
        upper += 1

print("Closest Fibonacci number:", closest_fibonacci(num))