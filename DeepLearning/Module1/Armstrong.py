num = int(input("Enter a number: "))

def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    return num == sum(int(d) ** power for d in digits)

def closest_armstrong(n):
    if n < 0:
        return None
    lower = n
    upper = n
    while True:
        if lower >= 0 and is_armstrong(lower):
            return lower
        if is_armstrong(upper):
            return upper
        lower -= 1
        upper += 1

result = closest_armstrong(num)
print("Closest Armstrong number:", result)