def convertion():
	inp=input("Enter the string: ")
	print(inp.upper())
	print(inp.lower())

	"""_______String convertion to number_______"""
	for x in inp:
		"""Converting charecters except special-ones(not recommended)

		if int(x,base=36):
			print(int(x,base=36),end="")
		"""	

		"""____Recommended____"""
		print(ord(x),end="")#--->ord() is used to convert any character according to ASCII
		
	print(end="\n")

	print(inp) #printing the normal string
	converting() #recursive-call

converting()