def test(lst):
    result = {}
    for item in lst:
        result[item[0]] = item[1:]
    return result

li = [["Bean", 10], ["Jack", 12], ["James", 11]]

print("Original list of lists:", li)
print("Converted lists to a dictionary:", test(li))