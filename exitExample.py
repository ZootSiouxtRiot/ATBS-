#EXIT PROG

import sys

while True:
  print('Type EXIT to exit.')
  response = input()
  if response == 'EXIT':
    sys.exit()
  print('You typed ' + response + '.')
