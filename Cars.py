#Getting the answer
n=input('Which car do you like the most? Hatchback ,Sedan or SUV :')
if n=='Hatchback' :
    a=input('Choose one of the following hatchbacks: Mazda 3 , Toyota Yaris :')
    if a=='Mazda 3' :
        print('You like a good hatchback with a affordable price!!! ')
    elif a == 'Toyota Yaris' :
        print('You like a hatchback that Toyota has stopped producing.')
    else :
        print('You do not choose options from what we give you!!!')
elif n == 'Sedan' :
    b=input('Choose one of the following sedans : Rolls royce phantom, Toyota Coroalla :')
    if b == 'Rolls royce phantom' :
        print("You like the world's most costliest sedan!!!")
    elif b == 'Toyota Coroalla' :
        print("You like an affordable and good sedan.")
    else :
        print('You do not choose from our options!!!')
elif n == 'SUV' :
    c=input('Choose one of the following SUVs : Rolls Royce Cullinan, Nissan Magnite :')
    if c == 'Rolls Royce Cullinan' :
        print('You like the costliest SUV by Rolls Royce.')
    elif c == 'Nissan Magnite' :
        print('You like a cheap and best SUV that is for families')
    else :
        print('You do not follow our opitions!!!')
else :
    print('That is not part of our options that we gave!!!')
#Bye-bye
print('Bye bye see you soon!!!')