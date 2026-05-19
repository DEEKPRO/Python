class person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def display(self):
        print(f"Your full name is {self.fname} {self.lname}")

class son(person):
    def __init__(self, fname, lname, year):
        self.year = year
        super().__init__(fname, lname)

obj = son("David", "Robins", "1989")
obj.display()
print(f"He graduated at {obj.year}")