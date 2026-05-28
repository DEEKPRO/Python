cod = open("C:\Deekshith\DeekPython\Python\DeepLearning\Module3\Lesson2\Codingal.txt", "r")
odd = open("C:\Deekshith\DeekPython\Python\DeepLearning\Module3\Lesson2\odd.txt", "w")
cont = cod.readlines()
for i in range(1, len(cont)+1):
    if(i%2!=0):
        odd.write(cont[i-1])
    else:
        pass

odd.close()

odd = open("C:\Deekshith\DeekPython\Python\DeepLearning\Module3\Lesson2\odd.txt", "r")
print(odd.read())