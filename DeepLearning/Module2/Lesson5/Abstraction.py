from abc import abstractmethod, ABC

class animal(ABC):
    def move(self):
        pass

class bird(animal):
    def move(self):
        print("This is a good bird.")
class dog(animal):
    def move(self):
        print("This is a good dog.")
class cat(animal):
    def move(self):
        print("This is a good cat.")

obj1, obj2, obj3 = bird(), dog(), cat()
obj1.move()
obj2.move()
obj3.move()