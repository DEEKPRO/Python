file = open("C:\Deekshith\DeekPython\Python\DeepLearning\Module3\Lesson3\codingal.txt", "x")
file.close()
file = open("C:\Deekshith\DeekPython\Python\DeepLearning\Module3\Lesson3\codingal.txt", "w")
file.write("Codingal is on a mission to inspire school kids to fall in love with coding.\nCoding helps develop logical thinking and problem-solving skills. \nCoding jobs are the future. \nThey already constitute more than 60% of all the jobs in Science, Technology, Engineering, and Math. \nWhile still in school, those who start young will be ahead of everyone by the time they get into college. \nThey will be creators of the future.\nDo you want to join us too?")
file.close()
with open("C:\Deekshith\DeekPython\Python\DeepLearning\Module3\Lesson3\codingal.txt") as file:
    data = file.readlines()
    for cod in data:
        cod = cod.split("\n")
        print(cod)