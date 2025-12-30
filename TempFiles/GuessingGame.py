d = input('Guess a word: ')
e = ['Jaguar', 'Leopard', 'Lion', 'Tiger', 'Chicken', 'Lamb', 'Panther', 'Cheetah']
compare = [i for i in e if d in e]
while d not in e:
    if len(compare) == 0:
        print('The word is wrong!')  
        d = input('Guess a word: ')
print('You got the word!')