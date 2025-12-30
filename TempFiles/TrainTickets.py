d = int(input('How many train tickets wanted: '))
e = {}
for i in range(d):
    a = input('Name and which train: ')
    name, train = a.split()
    e[name] = train
    print(f'Thank you {name}')
    print(f'Train ticket: {name} is going on {train}')
r = e.items()
for name, train in r:
    print(f"{name}'s {train} has arrived. When you are inside show them your train ticket!")
    print(f'Thank you {name} for choosing {train}')