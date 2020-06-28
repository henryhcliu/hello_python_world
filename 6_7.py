# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 22:01:52 2020

@author: 13034
"""


dic_name0 = {'first_name': 'Jackey',
            'last_name': 'Chan',
            'age': 22,
            'city': 'Shenyang'}
dic_name1 = {'first_name': 'Bluse',
            'last_name': 'Lee',
            'age': 23,
            'city': 'New York'}
dic_name2 = {'first_name': 'Li',
            'last_name': 'Lianjie',
            'age': 24,
            'city': "Xi'an"}

people = [dic_name0, dic_name1, dic_name2]

for person in people:
    print(' - ' + str(person))
    
print(people)