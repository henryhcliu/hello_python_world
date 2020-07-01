# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 11:48:00 2020

@author: 13034
"""
def judge(x):
    if x == 'quit' or x == 'q':
        return False
    else:
        return True


audience_age = input('Please input your age: ')

flag = True

flag = judge(audience_age)

while 1:
    audience_age = int(audience_age)
    if audience_age < 3:
        print('You can watch the video for free!')
    elif audience_age < 12:
        print('You need to pay $10.')
    else:
        print('You need to pay $15. ')
    
    audience_age = input('Please input your age: ')
    
    flag = judge(audience_age)
    if flag == False:
        break

print('\nThank you for your coopration!\nHave a good time watching.')
