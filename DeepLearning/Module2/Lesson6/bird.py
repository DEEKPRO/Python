class bird:
    def __init__(self, name, age, canfly):
        self.name = name
        self.age = age
        self.canfly = canfly
        canfly = bool(canfly)
    def fly(self):
        print("I see everything.")
    def walk(self):
        print("I feel tiny.")
    def sleep(self):
        print("I dream of nuts.")
    def perch(self):
        print("I feel taller.")

class parrot(bird):
    def __init__(self, name, age, canfly):
        super().__init__(name, age, canfly)
    def fly(self):
        print("I see everything.")
    def walk(self):
        return super().walk()
    def sleep(self):
        return super().sleep()
    def perch(self):
        return super().perch()

obird = bird("Timmy", "2", "True")
parr = parrot("Jimmy", "1", "False")

for bir in (obird, parr):
    bir.fly()
    bir.walk()
    bir.sleep()
    bir.perch()