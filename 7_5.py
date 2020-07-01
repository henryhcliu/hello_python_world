# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 11:42:47 2020

@author: 13034
"""


audience_age = input('Please input your age: ')
while audience_age != 'quit':
    audience_age = int(audience_age)
    if audience_age < 3:
        print('You can watch the video for free!')
    elif audience_age < 12:
        print('You need to pay $10.')
    else:
        print('You need to pay $15. ')
    
    audience_age = input('Please input your age: ')
print('\nThank you for your coopration!\nHave a good time watching.')
