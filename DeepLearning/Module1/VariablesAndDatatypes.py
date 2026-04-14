name = "Late Gickers"
age = 10
is_student = True
weight = 5.123456789
print("Name:", name, type(name))
print("Age :", age, type(age))
print("Is Student:", is_student, type(is_student))
print("Weight:", weight, type(weight))
print("After type casting ...\n")
age = str(age)
weight = int(weight)
print("Age :", age, type(age))
print("Weight:", weight, type(weight))