name = input("Hello! I am an AI chatbot. Tell me your name:\n")
mood = input("How do you feel?\n")
hobby = input("What is one of your hobbies?\n")

print(f"Hey {name}, {hobby} sounds fun!")

magic = input("Do you want to see a magic trick? (yes or no)\n").lower()

while magic == "yes":
    print("Think of a number in your head between 0 and 100.")
    print("Now multiply it by 2.")
    print("Add 8 to the result.")
    print("Divide by 2.")
    print("Now subtract your original number.")
    print("The answer is... 4! 🎩✨")
    
    magic = input("Do you want to see the magic trick again? (yes or no)\n").lower()

print("Okay, no more magic. Have a great day!")