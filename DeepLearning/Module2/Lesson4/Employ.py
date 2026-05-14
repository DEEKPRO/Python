class employee:
    def __init__(self, name, exp):
        self.name = name
        self.exp = exp
    def __del__(self):
        print("You just fired someone. Congratulations!")

jef = employee("Jeff", "20")
tim = employee("Tim", "3")

print(f"{jef.name}\n{tim.name}")
print(f"{jef.exp}\n{tim.exp}")
del tim
print("He has been fired for deleting the company code.")