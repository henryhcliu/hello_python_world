# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 19:30:27 2020

@author: 13034
"""


Beijing = {'country':'China',
           'population':'1 million',
           'fact':'Capital of China'}

London = {'Country':'UK',
          'Population':'0.6 million',
          'fact':'Capital of UK'}

Cities = {'Beijing': Beijing,
          'London': London}

for city_key, city_value in Cities.items():
    print(city_key.title()+' has the situation:' +str(city_value))