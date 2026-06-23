scores = [12, 25, 33, 41, 50, 67, 72, 85, 92, 98]
n, target = len(scores), 98
print(f"=== Quiz Score Finder(n = {n} scores) ===")
print(f"Scores: {scores}| Target: {target}")
print("\n")

#Linear Search
steps = 0
for i in range(n):
    steps += 1
    if scores[i] == target:
        print(f"Linear Search    : index = {i}| steps = {steps}| O(n)")
        break

#Binary Search(Iterative)

lo, hi, steps = 0, n - 1, 0
while lo <= hi:
    mid = (lo + hi) // 2
    steps += 1
    if scores[mid] == target:
        print(f"Binary Search    : index = {mid}| steps = {steps}| O(log n)")
        break
    elif scores[mid] < target:
        lo = mid + 1
    else:
        hi = mid - 1
print("\n")

#Binary Search(Recursive)
def binary_search(scores, lo, hi, target, calls=0):
    calls += 1
    if lo > hi:
        return -1, calls
    mid = (lo + hi) // 2
    if scores[mid] == target:
        return mid, calls
    elif scores[mid] < target:
        return binary_search(scores, mid + 1, hi, target, calls)
    else:
        return binary_search(scores, lo, mid - 1, target, calls)

result, calls = binary_search(scores, 0, n - 1, target)
print(f"Recursive Search : index = {result}| calls = {calls}| O(log n)")
print("\n")

print("=== Space and Complexity Summary ===")
print("Iterative : O(1) space - only lo, hi, mid")
print(f"Recursive : O(log n) space - {calls} stack frames for n = {n} scores")
print("\n")
print(f"Complexity ladder (n = {n}): ")
print("O(1)     : 1 step   - constant, never grows")
print(f"O(log n): {steps} - halving, grows slowly")
print(f"O(n)    : {n} steps - linear, grows with n")
print(f"O(n^2)  : {n*n} steps - quadratic, grows fast")
