# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 22:31:27 2020

@author: 13034
"""
def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    magicians_copy = []
    for magician in magicians:
        magicians_copy.append('The great '+ magician)
    return magicians_copy

magicians = ['Liu Qian', 'Zhu Chaoyang', 'Zhang Dongsheng']

show_magicians(magicians)
make_great(magicians[:])

print(magicians)
magicians = make_great(magicians)
print(magicians)