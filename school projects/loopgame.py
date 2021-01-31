# #task 1
# from math import pow
# i = 1
# a = int(input('Enter in a number: '))
# while i <= a:
#     print(pow(i,2))
#     i += 1

#task 2 guessing number game

import random

answer = 'y'

guess = -1

while answer == 'y':
    number = (random.randint(0,9))
    print('\nThe computer has chosen a number from 0-9.')
    while guess != number:
        guess = int(input('\nEnter your guess: '))
        if guess > number:
            print('Too high!')
        elif guess < number:
            print('Too low!')
        else:
            print('You got it!\n')
    answer = input('Would you like to play again? Enter y for yes and n for no: ')