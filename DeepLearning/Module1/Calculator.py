inp = int(input("Enter which operator you want to use(1-add,2-sub,3-mul,4-div): "))
def addition():
    print('Type 0 when you want to end.')
    e = [0]
    temp =0
    while e:
        d = int(input('Type in the number:'))
        if d == 0:
            break
        e.append(d)
        temp=temp+d
    return temp

def subtraction():
    f = int(input('Type the first number : '))
    s = int(input('Type the second number : '))
    if f<=s :
        return s - f
    else:
        return f-s

def multiplication():
    e = [1]
    temp = 1
    while e:
        d = int(input('Type in the number: '))
        if d == 0:
            break
        e.append(d)
        temp = temp*d
    return temp

def division():
    print('This is Division. We will divide only two numbers.')
    f = int(input('Type the first number : '))
    s = int(input('Type the second number : '))
    if f<=s:
        return s/f
    else:
        return f/s

if inp == 1:
    print(addition())
elif inp == 2:
    print(subtraction())
elif inp == 3:
    print(multiplication())
elif inp == 4:
    print(division())
else:
    print("No calculator for u.")