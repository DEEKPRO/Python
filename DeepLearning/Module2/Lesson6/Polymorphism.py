class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"My name is {self.name} and I am {self.age} old.")
    def make_sound(self):
        print("Woof! Woof!")

class cat:
    def __init__(self, name , age):
        self.name = name
        self.age = age
    def info(self):
        print(f"My name is {self.name} and I am {self.age} old.")
    def make_sound(self):
        print("Meow! Meow!")

odog = dog("Jimmy", "3")
ocat = cat("Jim", "1")

for animal in (odog, ocat):
    animal.info()
    animal.make_sound()