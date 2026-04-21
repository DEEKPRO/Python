import sympy as sp

num = int(input("Enter a number: "))

ans = sp.isprime(num)
if ans == True:
    print("The number is prime.")
else:
    print("The number isn't prime.")