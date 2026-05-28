cod = open("C:\Deekshith\DeekPython\Python\DeepLearning\Module3\Lesson2\Codingal.txt", "r")
fil = open("C:\Deekshith\DeekPython\Python\DeepLearning\Module3\Lesson2\sile.txt", "r")
print(cod.read(), "\n", fil.read())
fil.close();cod.close()
cod = open("C:\Deekshith\DeekPython\Python\DeepLearning\Module3\Lesson2\Codingal.txt", "r")
fil = open("C:\Deekshith\DeekPython\Python\DeepLearning\Module3\Lesson2\sile.txt", "w")
for line in cod.readlines():
    if not line.startswith("Coding"):
        print(line)
        fil.write(line)
fil.close();cod.close()
