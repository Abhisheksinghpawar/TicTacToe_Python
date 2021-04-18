board = ["","","","","","","","","",""]
status = ""
user_inputs = [0]

def update_board_x(pos_x):
    board[pos_x] = "X"

def update_board_o(pos_o):
    board[pos_o] = "O"

def winner_check_x():
    print("\n" * 35)
    print("",board[7]," | ",board[8]," | ",board[9],"\n","-------------","\n",board[4]," | ",board[5]," | ",board[6],"\n","-------------","\n",board[1]," | ",board[2]," | ",board[3])
    if (board[1] == board[2] == board[3] == "X" or
    board[4] == board[5] == board[6] == "X" or
    board[7] == board[8] == board[9] == "X" or
    board[1] == board[4] == board[7] == "X" or
    board[2] == board[5] == board[8] == "X" or
    board[3] == board[6] == board[9] == "X" or
    board[1] == board[5] == board[9] == "X" or
    board[3] == board[5] == board[7] == "X"):
        print("X won the Game")
        return "game over"

def winner_check_o():
    print("\n" * 35)
    print("",board[7]," | ",board[8]," | ",board[9],"\n","-------------","\n",board[4]," | ",board[5]," | ",board[6],"\n","-------------","\n",board[1]," | ",board[2]," | ",board[3])
    if (board[1] == board[2] == board[3] == "O" or
    board[4] == board[5] == board[6] == "O" or
    board[7] == board[8] == board[9] == "O" or
    board[1] == board[4] == board[7] == "O" or
    board[2] == board[5] == board[8] == "O" or
    board[3] == board[6] == board[9] == "O" or
    board[1] == board[5] == board[9] == "O" or
    board[3] == board[5] == board[7] == "O"):
        print("O won the Game")
        return "game over"

print('''

Welcome to the Tic Tac Toe Game !!!

7|8|9
4|5|6
1|2|3
''')

while True:
    if status != "game over":
        while True:
            try:
                pos_x = int(input("Player 1 Enter ( X ): "))
                while pos_x in user_inputs:
                    print("already exists")
                    pos_x = int(input("Player 1 Enter ( X ): "))
                else:
                    user_inputs.append(pos_x)
            except:
                print("Invalid input")
            else:
                break
        update_board_x(pos_x)
        status = winner_check_x()
    else:
        break
    if status != "game over":
        while True:
            try:
                pos_o = int(input("Player 2 Enter ( O ): "))
                while pos_o in user_inputs:
                    print("already exists")
                    pos_o = int(input("Player 2 Enter ( O ): "))
                else:
                    user_inputs.append(pos_o)
            except:
                print("Invalid input")
            else:
                break
        update_board_o(pos_o)
        status = winner_check_o()
    else:
        break
