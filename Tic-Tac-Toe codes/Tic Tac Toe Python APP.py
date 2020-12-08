game_still_going_on = True
winner = None
current_player = "X"

board = ['_','_','_',
        '_','_','_',
        '_','_','_']

def display_board():
        print("|"+board[0]+"|"+board[1]+"|"+board[2]+"|")
        print("|"+board[3]+"|"+board[4]+"|"+board[5]+"|")
        print("|"+board[6]+"|"+board[7]+"|"+board[8]+"|")

display_board()

def play_game():
        handle_turn1(current_player)

def handle_turn1(player):
        print(player+"'s turn.")
        position1 = input("Chose a position from 1-9: ")

        while position1 not in ["1","2","3","4","5","6","7","8","9"]:
                print("Invalid input!")
                position1 = input("Chose a position from 1-9: ")

                position1 = int(position1) - 1

        if board[position1] == "_":
                board[position1] = player
        elif board[position1] == "X":
                while position1 not in ["1","2","3","4","5","6","7","8","9"]:
                        print("Invalid input!")
                        position1 = input("Chose a position from 1-9: ")
        display_board()

        

def check_game_is_over():
        check_if_winner()
        check_if_tie()

def check_if_winner():
        global winner
        
        row_winner = check_rows()
        column_winner = check_columns()
        diagonal_winner = check_diagonals()

        if row_winner:
                winner = row_winner
        elif column_winner:
                winner = column_winner
        elif diagonal_winner:
                winner = diagonal_winner

        return

def check_rows():
        global game_still_going_on
        
        row1 = board[0]==board[1]==board[2] != "_"
        row2 = board[3]==board[4]==board[5] != "_"
        row3 = board[6]==board[7]==board[8] != "_"

        if row1 or row2 or row3:
                game_still_going_on = False

        if row1:
                return board[0]
        elif row2:
                return board[3]
        elif row3:
                return board[6]
        return

def check_columns():
        global game_still_going_on
        
        col1 = board[0]==board[3]==board[6] != "_"
        col2 = board[1]==board[4]==board[7] != "_"
        col3 = board[2]==board[5]==board[8] != "_"

        if col1 or col2 or col3:
                game_still_going_on = False

        if col1:
                return board[0]
        elif col2:
                return board[1]
        elif col3:
                return board[2]
        return

def check_diagonals():
        global game_still_going_on
        
        dia1 = board[0]==board[4]==board[8] != "_"
        dia2 = board[2]==board[4]==board[6] != "_"

        if dia1 or dia2:
                game_still_going_on = False

        if dia1:
                return board[0]
        elif dia2:
                return board[2]

        
        return



def check_if_tie():
        global game_still_going_on

        if "_" not in board:
                print("Tie.")
                game_still_going_on = False

def flip_player():
        global current_player

        if current_player == "X":
                current_player = "0"
        elif current_player == "0":
                current_player = "X"
        return



while game_still_going_on:
        play_game()
        check_game_is_over()
        flip_player()

        if winner=="X" or winner=="0":
                print(winner+" won")
        elif winner==None:
                print("Tie.")
        
