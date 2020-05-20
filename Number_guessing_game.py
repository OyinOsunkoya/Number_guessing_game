#Number guessing game
import random as rd 

#gen random integer between 1 and 100
i = rd.randint(1,100)
#print(i) #delete this
for guess in range(5):
    guess=input('Enter a whole number/ integer between 1 and 100:')
    try:
        guess=int(guess)
    except:
        print('Please input a valid number!!')
        continue
    if guess== i:
        print('Congrats!!!, You guessed right')
        break
    elif i-5<guess and guess<i+5:
        print('Hmm!, You are quite close')
    elif guess<i:
        print("You need to guess higher")
    elif guess>i:
        print("You need to guess lower")
print('The number chosen by the computer was {}'.format(i))
