di1 = {1:"apple",2:"banana",3:"orange",4:"watermelon",5:"strawberry"}
di2 = {"a":0,"b":["banana", "apple", "papaya", "orange", "strawberry"]}
di3 = {"a":"b", "c":3}
print(di1[4])
print(di3.get("c"))
print(di2["b"][2])
di3["c"] = 90
print(di3)
di3["d"] = "dinosaur"
print(di3)
di1.pop(5)
print(di1)
di1.clear()
print(di1)