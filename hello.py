# This program pulls the current date and time (remotely), says hello, asks for their name,
# calculates the length in characters of their name,
#and calcs their age in the year 2050.

print('The current date and time is:')

import urllib.request
url = "http://just-the-time.appspot.com/"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
print (response.read().decode('utf-8'))

print('What is your first name?') # asks for the user's first name
myFirstName = input()

print('What is your last name?')  # asks for the user's last name
myLastName = input()

print('Thank you', myFirstName, myLastName'.)

print('The length of your full name is: ')
print(len(myFirstName + myLastName))

print('What is your age?')     # asks for user's age
myAge = input()

print(myFirstName, myLastName)
print('You will be ' + str(int(myAge) + 31) + ' in the year 2050. Congratulations!')

# print('You were born in '  + 2050 - str(int(myAge)))
      
      
      
  
