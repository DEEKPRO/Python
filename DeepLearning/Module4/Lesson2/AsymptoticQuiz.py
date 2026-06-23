# Asymptotic Quiz

#In this assignment, you will build a Quiz Result Searcher using Python. 
#They will compare three different ways of working with quiz scores: 
#direct access
#linear search
#pair comparison. 
#Through these examples, students will understand asymptotic analysis, Big-O, Omega, Theta, best case, average case, worst case
#and the difference between O(1), O(n), and O(n^2).

#Quiz scores for 10 students
student_names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"]
quiz_scores = [85, 92, 78, 90, 88, 95, 80, 91, 87, 89]
for i in range(len(student_names)):
    print(f"{student_names[i]}: {quiz_scores[i]}")

#1. Direct Access (O(1))
target_student = "Alice"
steps = 1
print(f"Direct Access: {target_student} found at index 1. It is always 1 for direct access.")

#2. Linear Search (O(n))
target_student = "Eve"
steps = 0
for i in range(len(student_names)):
    steps += 1
    if target_student == student_names[i]:
        print(f"Linear Search: {target_student} found at index {i}. This is equal to n in the worst case.")
print(f"Linear Search: {target_student} found after {steps} steps.")

#3. Pair Comparison (O(n^2))
target_student = "Judy"
steps = 0
for i in range(len(student_names)):
    for j in range(i + 1, len(student_names)):
        steps += 1
        if student_names[i] == target_student:
            pass
print(f"Pair Comparison: {target_student} found at index {i}. This is equal to n^2 in the worst case.")
print(f"Pair Comparison: {target_student} found after {steps} steps.")

#For the next three sections, linear search will be uesd as an example.

#Big O
print("Big O Notation:")
target_student = "Judy"
steps = 0
for i in range(len(student_names)):
    steps += 1
    if target_student == student_names[i]:
        break
print(f"Big O: {target_student} found after {steps} steps. This is O(n) in the worst case.")

#Omega
print("Omega Notation:")
target_student = "Alice"
steps = 0
for i in range(len(student_names)):
    steps += 1
    if target_student == student_names[i]:
        break
print(f"Omega: {target_student} found after {steps} steps. This is Omega(1) in the best case.")

#Theta
print("Theta Notation:")
target_student = "Eve"
steps = 0
for i in range(len(student_names)):
    steps += 1
    if target_student == student_names[i]:
        break
print(f"Theta: {target_student} found after {steps} steps. This is Theta(n) in the average case.")

#Summary
print("Summary:")
print("Direct Access: O(1) - Always 1 step.")
print("Linear Search: O(n) - Always n steps in the worst case.")
print("Pair Comparison: O(n^2) - Always n^2 steps in the worst case.")
print("\n")
print("Big O: O(n) - Worst case for linear search.")
print("Omega: Omega(1) - Best case for linear search.") 
print("Theta: Theta(n) - Average case for linear search.")
print("\nEND OF QUIZ")
