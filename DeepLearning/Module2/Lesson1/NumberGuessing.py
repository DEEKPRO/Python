import random as ran

num = int(input("Enter the highest number that can be guessed: "))
x = 1
y = ran.randint(x, num)

while True:
    ans = int(input("Enter your guess: "))
    while ans != y:
        if ans > y:
            print("Your guess is greater than the MYSTERY NUMBER")
            break
        elif ans < y:
            print("Your guess is less than MYSTERY")
            break
    if ans == y:
        print("You guessed it!")
        break