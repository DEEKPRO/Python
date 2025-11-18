print('This is Addition. We will add infinite numbers.')
print('Type 0 when you want to end.')
e = [0]
temp =0
while e:
    d = int(input('Type in the number:'))
    if d == 0:
        break
    e.append(d)
    temp=temp+d
print(f'Total: {temp}')