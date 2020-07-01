# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 19:37:35 2020

@author: 13034
"""


num = input('Please input a number: ')
if int(num)%10 == 0:
    print('This number: '+str(num)+' is an integer of ten')
else:
    print('This number: '+str(num)+' is not an integer of ten')