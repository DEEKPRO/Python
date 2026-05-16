class express:
    def __init__(self,num1,num2,num3):
        num1, num2, num3 = int(num1), int(num2), int(num3)
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
    def add(self):
        add = self.num1+self.num2+self.num3
        return add
    def subtract(self):
        sub = self.num1-self.num2-self.num3
        return sub

n = input("Enter num1: ")
nu = input("Enter num2: ")
num = input("Enter num3: ")

expe = express(n, nu, num)
print(expe.add())
print(expe.subtract())