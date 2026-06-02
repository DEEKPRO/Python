import os
with open("C:\Deekshith\DeekPython\Python\DeepLearning\Module3\Lesson3\example.txt", "x") as file:
    file.close()
if os.path.exists("C:\Deekshith\DeekPython\Python\DeepLearning\Module3\Lesson3\example.txt"):
    os.remove("C:\Deekshith\DeekPython\Python\DeepLearning\Module3\Lesson3\example.txt")
else:
    print("File doesn't exist")

with open("C:\Deekshith\DeekPython\Python\DeepLearning\Module3\Lesson3\codingal.txt", "w") as file:
    file.write("This is the first line.")
    file.write("This is the second line.")
    file.write("This is the third line.")
    file.close()

os.rmdir("C:\Deekshith\DeekPython\Python\DeepLearning\Module3\Lesson3\iandom")