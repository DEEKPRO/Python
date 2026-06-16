n = 4
print("=== Counting Game Points (n = ",n," rounds) ===")

total = n * (n+1) // 2
print(f"Formula Way: Total = {total}| steps = 1")

total = 0
steps = 0
for round_num in range(1, n + 1):
    total += 1
    steps += 1
print(f"-Looped Way: Total = {total}| steps = {steps}")

total = 0
steps = 0
for round_num in range(1, n+1):
    for point in range(1, round_num+1):
        total += 1
        steps += 1
print(f"-Nested Way: Total = {total}| steps = {steps}")

n = 10
nested_steps = 0
for round_num in range(1, n+1):
    for point in range(1, round_num+1):
        nested_steps += 1

print()
print(f"=== Now with n = {n} rounds ===")
print(f"Formula way: steps = 1                 (always just 1)")
print(f"-Looped way: steps = {n}")
print(f"-Nested way: steps = {nested_steps}     (grows much faster)")
print()
print("Same answer - but very different costs. That is time complexity.")