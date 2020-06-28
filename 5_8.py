# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 15:48:12 2020

@author: 13034
"""

# 5.8 - 5.10

current_users = ['usr1', 'usr2','usr3','usr4','admin']
#current_users = []
if current_users == []:
    print('We need to find some users!')


else:
    usr = input('Please input your user name:')
    if usr in current_users:
        if usr == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print('Hello '+usr+', thank you for logging in again!') 
    else:
        print('Please check your user name again!')
        
        
    new_users = current_users[:]
    new_users.pop(3)
    new_users.append('Jackie Chan')
    new_users.append('Liu Haichao')
    current_users_lower = []
    for curr in current_users:
        current_users_lower.append(curr.lower())
    for new_user in new_users:
        if new_user.lower() in current_users_lower:
            print('You need use another user name but not '+ new_user)
        else:
            print('Congratulations! You can use this nickname: '+new_user+'!')
    print(current_users)