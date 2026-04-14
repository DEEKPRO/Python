try:
    lower = int(input("Enter a number: "))
    upper = int(input("Enter a larger number: "))
except ValueError:
    print("U messed up a number")

print("Addition: ", upper+lower)
print("Subtraction: ", upper-lower)
print("Multiplication: ", upper*lower)
print("Division: ", upper/lower)
print("Exponents: ", upper**lower)
print("Floor Division: ", upper//lower)
print("Modulus: ", upper%lower)
print("Square Root: ", upper**0.5, lower**0.5)
print("Equal: ", upper==lower)
print("Greater than: ", upper>=lower)
print("Less than: ", upper<=lower)
print("Not equal: ", upper!=lower)

first = "Bald "
last = "Parrot"
fist = first + last
sad = ":sob: " * 10
n = "jog tildo"
print(len(n))
print(n[0])
print(n[6])
print(n[2:-1])