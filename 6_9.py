# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 19:25:38 2020

@author: 13034
"""


favourite_places = {'Liu Chao':['Shenyang','Weifang'],
                    'Zhu Chuanwu':['Yantai','Qinhuangdao']}

for f_p_key, f_p_value in favourite_places.items():
    print(f_p_key+"'s favorate place(s) is/are: "+str(f_p_value))