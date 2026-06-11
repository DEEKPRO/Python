import random

def compchoice(user):
    num = random.randint(1,3)
    if num == 1:
        choice = "ROCK"
    elif num == 2:
        choice = "PAPER"
    elif num == 3:
        choice = "SCISSORS"
    if user == choice:
        print("Its a tie.")

print(compchoice())