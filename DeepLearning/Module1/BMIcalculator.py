weight = int(input("Enter your weight: "))
height = int(input("Enter your height: "))
BMI = weight / (height/100)**2
print("Your BMI is ", BMI)

"""BMI <= 39.9: - obese

BMI <= 34.9 - over weight

BMI <= 24.9 - healthy

BMI <= 18.4 -underweight"""

if BMI <= 18.4:
    print("You are underweight.")
elif BMI <= 24.9:
    print("You are healthy.")
elif BMI <= 34.9:
    print("You are overweight.")
elif BMI <= 39.9:
    print("You are obese")
else:
    print("You are severly obese.")