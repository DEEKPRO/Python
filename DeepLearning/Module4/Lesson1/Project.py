#Running Lap Tracker

target_score = 100

#Direct way
score = 1
print(f"Direct way: Score: {score}| Score is always 1.| O(1)")

#Linear way
score = 0
for lap in range(1, target_score + 1):
    score += 1
print(f"Linear way: Score: {score}| Score is always equal to the target score.| O(n)")

#Quadratic way
score = 0
for lap1 in range(1, target_score + 1):
    for lap2 in range(1, target_score + 1):
        score += 1
print(f"Quadratic way: Score: {score}| Score is equal to the target score squared.| O(n^2)")