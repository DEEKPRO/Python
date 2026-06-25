
#Train Seat Finder
#In this python program, we will implement iterative binary search and recursive binary search
#to find a seat number in a train along with the names.

passengers = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"]
seat_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for seat in seat_numbers:
    if seat == 10:
        print(f"Seat Number: {seat}| Passenger: {passengers[seat-1]}")
    else:
        print(f"Seat Number: {seat} | Passenger: {passengers[seat-1]}")

target = 8
n = len(seat_numbers)
#Iterative Binary Search
lo, hi, steps = 0, n- 1, 0
while lo <= hi:
    mid = (lo + hi) // 2
    steps += 1
    if seat_numbers[mid] == target:
        print(f"Binary Search    : index = {mid}| steps = {steps}| O(log n)")
        break
    elif seat_numbers[mid] < target:
        lo = mid + 1
    else:
        hi = mid - 1
print("\n")

#Recursive Binary Search
def binary_search(seat_numbers, lo, hi, target, calls=0):
    calls += 1
    if lo > hi:
        return -1, calls
    mid = (lo + hi) // 2
    if seat_numbers[mid] == target:
        return mid, calls
    elif seat_numbers[mid] < target:
        return binary_search(seat_numbers, mid + 1, hi, target, calls)
    else:
        return binary_search(seat_numbers, lo, mid - 1, target, calls)

result, calls = binary_search(seat_numbers, 0, n - 1, target)
print(f"Recursive Search : index = {result}| calls = {calls}| O(log n)")
print("\n")

