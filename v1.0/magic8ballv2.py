#!/user/bin/env python3
###
"""
  magic_8_ballv2.py
  @author Andrej Saule
  @version 05-04-2019
"""

import random

def main():
        print('Magic 8 Ball predicts the future and helps you make decisions. Probably bad ones ;)')

        #Below is an index of replies, integers go from 0-3 inclusive
        replies = ['Yes','Signs point to yes',
                'Reply hazy ask again later',
                'I dont think so!','Definitely not!',
                ]


        #Loop function for asking question (will always loop because true)
        while True:
            #Get user to enter a question
            question = input('Enter a Yes/ No Question: ')

            #reply with a random Yes/ Maybe/ No response
            rand_value = int(random.random() * 5)   # returns number from 0-4 inclusive
            print(replies[rand_value])

            #Ask if they want to try again
            go_again = input('Would you like to ask another question? ')
            if go_again[0].lower() == 'n':
                break

        print ('Goodbye')


if __name__ == '__main__':
    main()
