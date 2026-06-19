# Big O, Omega, and Theta Notations in Algorithm Analysis

# The Leaderboard

names = ["Alice", "Bob", "Charlie", "David", "Eve"]
scores = [95,      85,    90,        80,      92]
n = len(scores)
print(f"Score Tracker (n = {n} players):")
for i in range(n):
    print(i+1, ". ", names[i], ":", scores[i], sep="")
print("\n")
# Theta Notation (Θ)

steps = 1
print(f"Score at index 0: {scores[0]} |Steps: {steps} |Theta(1) - tight bound")
print("\n")

# Omega (Ω) Notation

target = "Alice"
steps = 0
for name in names:
    steps += 1
    if name == target:
        break
print(f"Search for {target} |Steps = {steps} |Omega(1) - best case lower bound")
print("\n")

# Big O (O) Notation
target = "Eve"
steps = 0
for name in names:
    steps += 1
    if name == target:
        break
print(f"Search for {target} |Steps = {steps} |O(n) - worst case upper bound")
print("\n")

#Comparision of Notations
steps = 0
target_sum = 150
print(f"Pairs with the total score = {target_sum}:")
for i in range(n):
    for j in range(i+1, n):
        steps += 1
        if scores[i] + scores[j] == target_sum:
            print(f"{names[i]}+{names[j]} = {scores[i]} + {scores[j]}")

print(f"Total comparisions: {steps} | O(n^2) - drop constants, keep n^2")
print("\n")

#Asymptotic Analysis Summary
print("Asymptotic Analysis Summary:")
print("1. Theta (Θ)  : index access - always 1 step, tight bound")
print("2. Omega (Ω)  : best case, found in 1 step, lower bound")
print("3. Big O (O)  : worst case, found in n = ", n, "steps, upper bound")
print("4. Big O(n^2) : pair check - n*(n-1)/2 =", n*(n-1)//2, "comparisons")
print("\n")
print("Drop constants. Keep the dominant term. That is asymptotic analysis.")

