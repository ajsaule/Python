#!/user/bin/env python3
###
"""
  magic_8_ball.py
  @author Andrej Saule
  @version 05-04-2019
"""

import random

def main():
    print('Magive 8 Ball predicts the future and helps you make decisions. Probably bad ones ;)')

    #Get user to enter a question
    question = input('Enter a Yes/ No Question: ')

    #reply with a random Yes/ Maybe/ No response
    rand_value = int(random.random() * 4)   # returns numbe from 0-3 inclusive

    if rand_value == 0:
        print('Yes!')
    elif rand_value == 1:
        print('Signs point to Yes')
    elif rand_value == 2:
        print('Reply hazy. Ask again later')
    else:
        print('Not today friend')

if __name__ == '__main__':
    main()
