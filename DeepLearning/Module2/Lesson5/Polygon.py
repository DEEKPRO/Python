class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        side = int(side)
        self.side = side
    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        base = int(base)
        height = int(height)
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Rectangle(Shape):
    def __init__(self, length, width):
        length = int(length)
        width = int(width)
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        radius = int(radius)
        self.radius = radius
    def area(self):
        return 22/7 * (self.radius ** 2)

side = input("Side of Square: ")
length = input("Length of Rectangle: ")
width = input("Width of Rectangle: ")
height = input("Height of Triangle: ")
base = input("Base of Triangle: ")
radius = input("Radius of Circle: ")

for shape in (Square(side), Triangle(base, height), Rectangle(length, width), Circle(radius)):
    print(shape.area())