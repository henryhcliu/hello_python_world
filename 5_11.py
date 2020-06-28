# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 16:34:10 2020

@author: 13034
"""


list_nums = list(range(1,10))
print(list_nums)
for list_num in list_nums:
    if list_num == 1:
        print('1st')
    elif list_num == 2:
        print('2nd')
    elif list_num == 3:
        print('3rd')
    else:
        print(str(list_num)+'th')