try:
    swap = int(input("Enter a number: "))
    swapno = int(input("Enter a larger number: "))
except ValueError:
    print("U messed up a number")

a = swap 
swap = swapno
swapno = a
print(swap, "\n", swapno)