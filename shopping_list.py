shopping_list = []
total_ammount = 0
total_items = 0

while 1:
	item_name = input("Item name: ")

	if item_name=='ext':
		print('\n')
		print("---------------------------------------------------------",end='\n')

		for x in range(0,len(shopping_list)):
			print(f"{x+1}| {shopping_list[x][0]} => {shopping_list[x][1]}",end='\n')
			total_ammount += int(shopping_list[x][1])
		
		print("---------------------------------------------------------",end='\n')
		print(f"Total ammount: {total_ammount}",end='\n')
		print(f"Total items: {total_items}",end='\n')

		break

	item_peice = input("Item price: ")

	shopping_list.append([item_name,item_peice])

	print('\n')
	print("---------------------------------------------------------",end='\n')

	for x in range(0,len(shopping_list)):
		print(f"{x+1}| {shopping_list[x][0]} => {shopping_list[x][1]}",end='\n')
	
	print("---------------------------------------------------------",end='\n')
	print('\n')
	
	total_items += 1
