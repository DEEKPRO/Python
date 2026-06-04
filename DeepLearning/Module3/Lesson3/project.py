import os
with open("C:\Deekshith\DeekPython\Python\DeepLearning\Module3\Lesson3\ile3.txt", "w") as file:
    file.write("Mountains are massive and so are seas.")
    file.write("\nSeas are massive and so are mountains.")
    file.close()
with open("C:\Deekshith\DeekPython\Python\DeepLearning\Module3\Lesson3\ile3.txt", "r") as file:
    read = file.read()
    for i in read.split(" "):
        print(i)
    file.close()
if os.path.exists("C:\Deekshith\DeekPython\Python\DeepLearning\Module3\Lesson3\Myfile.txt"):
    print("This file exists.")
else:
    file = open("C:\Deekshith\DeekPython\Python\DeepLearning\Module3\Lesson3\Myfile.txt", "x")
    file.close()
with open("C:\Deekshith\DeekPython\Python\DeepLearning\Module3\Lesson3\Myfile.txt", "w") as file:
    file.write("Mountains are massive and so are seas.")
    file.write("\nSeas are massive and so are mountains.")
    file.close()
os.remove("C:\Deekshith\DeekPython\Python\DeepLearning\Module3\Lesson3\Myfile.txt")