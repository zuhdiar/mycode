#!/usr/bin/env python3
message = 'Your grade is '
print('enter your grade in numbers: ')
grade= int(input())

if grade in range(1,100) and grade >=90:
    message = message + 'A'
elif grade in range(1,100) and grade >=89:
    message = message + 'B'
elif grade in range(1,100) and grade >=79:
    message = message + 'C'
elif grade in range(1,100) and grade >=69:
    message = message + 'D'
elif grade in range(1,100) and grade <=59:
    message = 'Sorry Sweetie! you failed!'

print (message)
exit
~                       
