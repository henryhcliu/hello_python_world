pizza_styles = ['New York Style', 'Chicago Style', \
'California Style']
for pizza_style in pizza_styles:
	#print(pizza_style)
	print('I like ' + pizza_style + ' pizza.')
print('I really love pizza!')

# 4.11
friend_pizzas = pizza_styles

pizza_styles.append('Laobeijing style')

friend_pizzas.append('Boston Style')

print('My favourite pizzas are'+str(pizza_styles))
print("My friend's favourite pizzas are"+ str(friend_pizzas))