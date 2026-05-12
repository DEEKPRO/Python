class parrot:
    species = "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age

tim = parrot("Tim","2")
rim = parrot("Jim","10")
print(f"{tim.name} is fighting with {rim.name}. One is aged, {tim.age}, while another's age is {rim.age}. This feels very unfair.")
print(tim.species, rim.species)