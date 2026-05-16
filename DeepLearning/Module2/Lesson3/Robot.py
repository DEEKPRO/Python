class Robot:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello! My name is {self.name}.")

rob1 = Robot("Tom")
rob2 = Robot("Jerry")

rob1.introduce()
rob2.introduce()
