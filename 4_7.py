
# 4.7
divisible_by_3 = range(3, 31, 3)
for num in divisible_by_3:
	print(num)

#4.8 & 4.9
cubic_operations = [value**3 for value in range(1,11)]
print(cubic_operations)

# 4.10
print('The first three items in the list are:'+str(cubic_operations[0:3]))

print('Three items from the middle of the list are:'+str(cubic_operations[3:6]))

print('The last three items in the list are:'+str(cubic_operations[7:10]))