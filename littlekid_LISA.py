#Simple verification script

name = input('Please enter your name: ')
if name == 'Lisa':
    print('Hi', name)

age = input('Please enter your current age: ')
if name == 'Lisa' and age == '56':
    print('Account verified. Please continue.')

if name != 'Lisa' or age != '56':
  print('Incorrect match.')
  

