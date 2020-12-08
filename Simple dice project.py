from random import*

dice = int(random() * 6)
result = dice + 1

"""The full expanded Code"""

# if result == 1:
# 	print(1)

# elif result == 2:
# 	o = 1
# 	while o < result:
# 		print("*")
# 		o +=1
# 	print(result)

# elif result == 3:
# 	o = 1
# 	while o < result:
# 		print("*")
# 		o +=1
# 	print(result)

# elif result == 4:
# 	o = 1
# 	while o < result:
# 		print("*")
# 		o +=1
# 	print(result)

# elif result == 5:
# 	o = 1
# 	while o < result:
# 		print("*")
# 		o +=1
# 	print(result)

# else:
# 	o = 1
# 	while o < result:
# 		print("*")
# 		o +=1
# 	print(result)

"""The shortcut,easy,best and appropiate Code"""

o = 1
if o == result:
	print(result)

elif o < result:
	while o < result:
		print("*")
		o += 1
if result > 1:
	print(result)