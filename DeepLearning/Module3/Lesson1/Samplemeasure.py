sample = open("C:\Deekshith\DeekPython\Python\DeepLearning\Module3\Lesson1\sample.txt", "r")
counter = 0
reader = sample.read()
spl = reader.split("\n")
for i in spl:
    if i:
        counter+=1
print(counter)