days = int(input("How many total working days were there: "))
absent = int(input("How many days were you absent: "))
per = absent/days
per = 1-per
per = per*100
if per >= 75:
    print("You are eligible for the exam.")
else:
    print("You aren't eligible for the exam.")