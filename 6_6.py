# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 21:41:13 2020

@author: 13034
"""


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

List_investigators = ['jen', 'sarah', 'edward', 'John']


for dic_key in List_investigators:
    if dic_key in favorite_languages.keys():
        print('Thank you for your coopration, '+dic_key.title() +'!')
    else:
        print("Would you please join the survey, "+ dic_key +'?')