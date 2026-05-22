class polygon:
    def __init__(self,area,perimeter):
        self.area = area
        self.perimeter = self.perimeter
    def area(self):
        square = side * 4
    def perimeter(self):
        pass

class square(polygon):
    side = int(input())
    def __init__(self, area, perimeter):
        super().__init__(area, perimeter)
    
class rectangle(polygon):
    pass
class triangle(polygon):
    pass
class circle(polygon):
    pass