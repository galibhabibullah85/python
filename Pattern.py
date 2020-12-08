def pattern(n):
	"""for i in range(1,n):
		for j in range(1,i):
			print("* ",end="")
		print("\r")"""

	"""for i in range(1,n+1):
		for j in range(1,n+1):
			print("* ",end="")
		print("\n")"""

	for i in range(n+1,1,-1):
		for j in range(1,n+1):
			print("* ",end="")
		print("\n")

pattern(4)