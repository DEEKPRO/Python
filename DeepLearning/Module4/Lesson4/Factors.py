num = int(input("Enter a number: "))

for i in range(1, num+1):
    divide = num % i
    if type(divide) == int and divide == 0:
        print(i)