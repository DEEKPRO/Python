class computer:
    def __init__(self):
        self.__price = 1500
    def sell(self):
        print(f"Current selling price: {self.__price}")
    def setmax(self, price):
        self.__price = price

buyer = computer()
buyer.sell()
buyer.__price = 2000
buyer.sell()
buyer.setmax(3000)
buyer.sell()
