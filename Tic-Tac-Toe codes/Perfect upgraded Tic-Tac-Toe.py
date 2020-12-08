print("\\                 /")
print(" \\   Let's play  /")
print("  \\ Tic-Tac-Toe /")
print("   \\           /")

	
def infinite():
	global current_turn
	condition = ['1','2','3','4','5','6','7','8','9','7865']

	d_board=[]
	w_board=[]

	for x in range(0,9):
		d_board.append(f" {x+1} ")
		w_board.append("_")



#..........................Playing with friends.........................

	def friend_mode():
		
		display_board()
		change_turn_until()
		

	def display_board():
		print("\n|"+d_board[0]+"|"+d_board[1]+"|"+d_board[2]+"|")
		print("|"+d_board[3]+"|"+d_board[4]+"|"+d_board[5]+"|")
		print("|"+d_board[6]+"|"+d_board[7]+"|"+d_board[8]+"|\n")


	
	#.......................Handling the turn...........................
	def play_turn(turn):
		current_turn = turn
		print("*****************"+current_turn+"'s turn*****************\n")
		
		inpt = input("Enter your position from 1-9: ")

		if inpt=="7865":
			win_denoting(current_turn)

		while inpt not in condition:
			inpt = input("Invalid input.Enter your position again from 1-9: ")

			if int(inpt)==7865:
				win_denoting(current_turn)

		while w_board[int(inpt)-1]!="_":
			inpt = input("Invalid input.Enter your position again from 1-9: ")
			if int(inpt)==7865:
				win_denoting(current_turn)

			while inpt not in condition:
				inpt = input("Invalid input.Enter your position again from 1-9: ")

				if inpt=='7865':
					win_denoting(current_turn)

		w_board[int(inpt)-1] = current_turn
		d_board[int(inpt)-1] = current_turn
		display_board()


	
	#.......................Changing the turn..........................
	def change_turn():
		for x in range(0,2):
			if x==0:
				play_turn(" X ")
				win_checking("X")

				if "_" not in w_board:
					game_tie()

			else:
				play_turn(" O ")
				win_checking("O")

		change_turn_until()



	#....................Checks if anyone wins.........................
	def win_checking(x):
		y = x
		row1=w_board[0]==w_board[1]==w_board[2]!="_"
		row2=w_board[3]==w_board[4]==w_board[5]!="_"
		row3=w_board[6]==w_board[7]==w_board[8]!="_"

		col1=w_board[0]==w_board[3]==w_board[6]!="_"
		col2=w_board[1]==w_board[4]==w_board[7]!="_"
		col3=w_board[2]==w_board[5]==w_board[8]!="_"

		dia1=w_board[0]==w_board[4]==w_board[8]!="_"
		dia2=w_board[2]==w_board[4]==w_board[6]!="_"

			
		if row1 or row2 or row3:
			win_denoting(y)

		elif col1 or col2 or col3:
			win_denoting(y)

		elif dia1 or dia2:
			win_denoting(y)


	
	#..........................Declares the winner.....................
	def win_denoting(x):
		print(f"------------------{x} wins!------------------\n")
		print("__________________Game Over!__________________\n\n")

		infinite()




	#........................Declares Tie...............................
	def game_tie():		
		print("__________________Game Tie!__________________\n")
		print("__________________Game Over!__________________\n\n")

		infinite()



	#..................Continuing the changes of turn..................
	def change_turn_until():
		change_turn()




#.......................Playing with Computer..........................
	def Computer_mode():
		ask_turn()




	#..................Asking turn choice...............................
	def ask_turn():
		print("Which turn you want to choose?")
		print("1 for X\n2 for O")
		input_com = int(input("Enter your choice: "))

		display_board_com()

		if input_com==1 or input_com==2:
			manage_turn_until(input_com)
		else:
			while input_com!=1 or input_com!=2:
				print("Invalid input.Please enter your choice correctly!")
				print("1 for X\n2 for O")
				input_com = int(input("Enter your choice: "))

				if input_com==1 or input_com==2:
					manage_turn_until(input_com)
				



	#.....................Displaying game board........................
	def display_board_com():
		print("\n|"+d_board[0]+"|"+d_board[1]+"|"+d_board[2]+"|")
		print("|"+d_board[3]+"|"+d_board[4]+"|"+d_board[5]+"|")
		print("|"+d_board[6]+"|"+d_board[7]+"|"+d_board[8]+"|\n")





	#......................Manage turns................................
	def manage_turn(x):
		if x==1:
			play_turn_human(" X ")
			win_checking_com(" X ")

			play_turn_com(" O ")
			win_checking_com(" Computer ")

			if "_" not in w_board:
				game_tie()

		elif x==2:
			play_turn_com(" X ")
			win_checking_com(" Computer ")

			play_turn_human(" O ")
			win_checking_com(" O ")

			if "_" not in w_board:
					game_tie()

		z = x
		manage_turn_until(z)




	#...................Infinite manageing turns........................
	def manage_turn_until(a):
		y = a
		manage_turn(y)




	#..................Handling the turn for human......................
	def play_turn_human(turn):
		current_turn = turn
		print("*****************"+current_turn+"'s turn*****************\n")
		
		inpt = input("Enter your position from 1-9: ")

		if inpt=='7865':
			win_denoting_com(current_turn)

		while inpt not in condition:
			inpt = input("Invalid input.Enter your position again from 1-9: ")
			if inpt=='7865':
				win_denoting_com(current_turn)

		while w_board[int(inpt)-1]!="_":
			inpt = input("Invalid input.Enter your position again from 1-9: ")

			while inpt not in condition:
				inpt = input("Invalid input.Enter your position again from 1-9: ")
				if inpt=='7865':
					win_denoting_com(current_turn)

		w_board[int(inpt)-1] = current_turn
		d_board[int(inpt)-1] = current_turn
		display_board_com()





	#.................Handling the turn for computer....................
	def play_turn_com(turn):
		current_turn = turn
		print("*****************Computer's turn*****************\n")

		from random import randint

		rand_inpt = randint(1,9)

		while(w_board[rand_inpt-1] !="_"):
			rand_inpt=randomIntegerGenerator()

		w_board[rand_inpt-1] = current_turn
		d_board[rand_inpt-1] = current_turn
		display_board_com()



	#......................Handling random input of Computer.......................
	def randomIntegerGenerator():
		from random import randint 

		randomInteger = randint(1,9) - 1

		return randomInteger

		# if w_board[randomInteger]=="_":
		# 		w_board[randomInteger] = turn_of_this_function
		# 		d_board[randomInteger] = turn_of_this_function
		# 		display_board_com()
		# else:			
		# 	play_turn_com(turn_of_this_function)




	#....................Checks if anyone wins.........................
	def win_checking_com(x):
		y = x
		row1=w_board[0]==w_board[1]==w_board[2]!="_"
		row2=w_board[3]==w_board[4]==w_board[5]!="_"
		row3=w_board[6]==w_board[7]==w_board[8]!="_"

		col1=w_board[0]==w_board[3]==w_board[6]!="_"
		col2=w_board[1]==w_board[4]==w_board[7]!="_"
		col3=w_board[2]==w_board[5]==w_board[8]!="_"

		dia1=w_board[0]==w_board[4]==w_board[8]!="_"
		dia2=w_board[2]==w_board[4]==w_board[6]!="_"

			
		if row1 or row2 or row3:
			win_denoting_com(y)

		elif col1 or col2 or col3:
			win_denoting_com(y)

		elif dia1 or dia2:
			win_denoting_com(y)


	
	#..........................Declares the winner.....................
	def win_denoting_com(x):
		print(f"------------------{x} wins!------------------\n")
		print("__________________Game Over!__________________\n\n")

		infinite()




	#........................Declares Tie...............................
	def game_tie():		
		print("__________________Game Tie!__________________\n")
		print("__________________Game Over!__________________\n\n")

		infinite()




	#..........................Asking mode.............................
	def ask_mode():
		print("\n\nWith whom you want to play?")
		print("1 for Computer \n2 for Your friend\n3 for exit")
		inpt = int(input("Please enter your choice: "))

		if inpt==2:
			friend_mode()
		elif inpt==1:
			Computer_mode()
		elif inpt==3:
			print("\n\n\tThank for playing.Have a nice day!")
			exit()
		else:
			while inpt!=1 or inpt!=2 or inpt!=3:
				print("\nInvalid input.Please input your choice correctly!")
				print("1 for Computer \n2 for Your friend\n3 for exit")
				inpt = int(input("Please enter your choice: "))

				if inpt==2:
					friend_mode()
				elif inpt==1:
					Computer_mode()
				elif inpt==3:
					print("\n\n\tThank for playing.Have a nice day!")
					exit()

	ask_mode()

infinite()