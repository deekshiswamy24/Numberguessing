#Python program to create a simple CLI project
#Numberguessing using random() function in python

#import a module called random
import random

#take inputs
#random.randint() generates only integer number between given range
num= random.randint(0,10)

#store that number in variable num and print it
print('Number:',num)

#number of attempts given to user
attempt =4

#if user uses all his attempts then print msg
msg = 'you lost'

#using while loop input the user guess
#if user guesses the number print msg
while attempt> 0:
    
    user = int(input('Guess the number'))

    if user==num:
        msg = 'you won!'
        break
    else :
        print(f'Try again! {attempt} attempt left.')
        attempt -=1
        continue

print(msg)
