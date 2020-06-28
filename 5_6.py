# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 15:30:48 2020

@author: 13034
"""


age = input('Please input your age:')
age = int(age)
if age < 2:
    print('You are a baby!')
elif age < 4:
    print('You are a toddler!')
elif age <13:
    print('You are a child!')
elif age < 20:
    print('You are a teenager!')
elif age < 65:
    print('You are an adult!')
else:
    print('You are an old people!')