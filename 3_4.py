# This code includes the practice of #3.4 - #3.7
# 3.4
# guests = ['Yue Suyun', 'Mu Chuanfa', 'Jang Yukun']
# for guest in guests:
# 	print('Mr/Ms '+guest+', if you can attend my dinner\
# , I would be very happy!')

# 3.5
def invite(guests):
	for guest in guests:
		print('Mr/Ms '+guest+', if you can attend my dinner\
, I would be very happy!')
	print()

guests = ['Yue Suyun', 'Mu Chuanfa', 'Jang Yukun']
# 3.5
# invite(guests)

# print(guests[0]+' can not attend the party, what a shame!')

# guests[0] = 'Zhang Xiao'
# invite(guests)

#3.6
guests.insert(0, 'Ma Zhankui')
guests.insert(1, 'Liu Xiaobo')
guests.append('Ma Li')
# invite(guests)
# 3.9 
print('I have invited '+str(len(guests))+' guests in \
this party!')
# 3.9 end
for i in range(2, len(guests)):
	sorry = guests.pop()
	print('Sorry, '+sorry+' can not come to the party now.')

invite(guests)

guests.pop()
guests.pop()
invite(guests)