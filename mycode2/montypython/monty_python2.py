#!/usr/bin/env python3

round=0
while(True):
    round=round+1
    print('finish the movie title, "monty python\'s the life of _____"')
    answer = input()
    if (answer.lower() =='brian'):
        print('correct')
        break
    elif (answer.lower() =='shrubbery'):
        print('you gave the super secret answer!')
        break
    elif (round ==3):
        print('sorry the answer was Brian.')
        break
    else:
        print('sorry. try again!')

