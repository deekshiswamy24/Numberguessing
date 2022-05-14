import random
num= random.randint(0,10)
print('Number:',num)
attempt =4
msg = 'you lost'
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
