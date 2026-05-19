class person:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def display(self):
        print(f"Your name is {self.name}")
        print(f"Your id is {self.id}")

class employee(person):
    def __init__(self,salary, role, name, id):
        self.salary = salary
        self.role = role
        super().__init__(name, id)

obj = employee("100k", "Mechanical Engineer", "Jeff", "192483")

obj.display()