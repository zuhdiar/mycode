#!/usr/bin/env python3
import sys

message = 'Your grade is '
print('enter your grade in numbers: ')
grade= input()

try:
    grade= float(grade)

except:
    print('dont try! just enter numbers between 1 and 100!')
    sys.exit()


if grade > 100:
    print("That number is higher than 100! Follow directions please.")
elif grade >=90:
    message = message + 'A'
elif grade >=89:
    message = message + 'B'
elif grade >=79:
    message = message + 'C'
elif grade >=69:
    message = message + 'D'
elif grade <=59:
    print("Sorry Sweetie! you failed!")
    sys.exit()
else:
    print('dont try! just enter numbers between 1 and 100!')
    sys.exit()
print (message)
