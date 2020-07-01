# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 22:48:58 2020

@author: 13034
"""


def intro_sandwiches(*toppings):
    print('You have ordered the toppings of sandwich:')
    for topping in toppings:
        print(' -'+topping)
        
intro_sandwiches('mushroom', 'banana', 'strawberry')
# You can add 2 more examples to satisfy the request of the problem.
