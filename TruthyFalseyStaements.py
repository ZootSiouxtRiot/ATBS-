name = ''
while not name:
  print('Enter your name:')
  name = input()

print('How many guests will you serving?')
numOfGuests = int(input())
if numOfGuests:
  print('REMINDER: Quote is good for 7 days from date of issue.')

print('Done.')
