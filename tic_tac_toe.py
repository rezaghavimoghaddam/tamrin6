import pyfiglet

def show():
    for  row in game_board:
        for cell in row:
            print(cell, " ", end="")
        print()

def check_game():
        if game_board[0][0] == "X" and game_board[0][1] == "X" and game_board[0][2] == "X":
            print("player1 wins!!")
        elif game_board[0][0] == "O" and game_board[0][1] == "O" and game_board[0][2] == "O":
            print("player2 wins!!")
        if game_board[1][0] == "X" and game_board[1][1] == "X" and game_board[1][2] == "X":
            print("player1 wins!!")
        elif game_board[1][0] == "O" and game_board[1][1] == "O" and game_board[1][2] == "O":
            print("player2 wins!!")
        if game_board[2][0] == "X" and game_board[2][1] == "X" and game_board[2][2] == "X":
            print("player1 wins!!")
        elif game_board[2][0] == "O" and game_board[2][1] == "O" and game_board[2][2] == "O":
            print("player2 wins!!")
        if game_board[0][0] == "X" and game_board[1][0] == "X" and game_board[2][0] == "X":
            print("player1 wins!!")
        elif game_board[0][0] == "O" and game_board[1][0] == "O" and game_board[2][0] == "O":
            print("player2 wins!!")
        if game_board[0][1] == "X" and game_board[1][1] == "X" and game_board[2][1] == "X":
            print("player1 wins!!")
        elif game_board[0][1] == "O" and game_board[1][1] == "O" and game_board[2][1] == "O":
            print("player2 wins!!")
        if game_board[0][2] == "X" and game_board[1][2] == "X" and game_board[2][2] == "X":
            print("player1 wins!!")
        elif game_board[0][2] == "O" and game_board[1][2] == "O" and game_board[2][2] == "O":
            print("player2 wins!!")
        if game_board[0][0] == "X" and game_board[1][1] == "X" and game_board[2][2] == "X":
            print("player1 wins!!")
        elif game_board[0][0] == "O" and game_board[1][1] == "O" and game_board[2][2] == "O":
            print("player2 wins!!")
        if game_board[0][2] == "X" and game_board[1][1] == "X" and game_board[2][0] == "X":
            print("player1 wins!!")
        elif game_board[0][2] == "O" and game_board[1][1] == "O" and game_board[2][0] == "O":
            print("player2 wins!!")
        if game_board[0][0] != "-" and game_board[0][1] != "-" and game_board[0][2] != "-" and game_board[1][0] != "-" and game_board[1][1] != "-" and game_board[1][2] != "-" and game_board[2][0] != "-" and game_board[2][1] != "-" and game_board[2][2] != "-":
            print("draw")

title = pyfiglet.figlet_format("Tic Tac Toe", font="slant")
print(title)

game_board = [["-", "-", "-"],
              ["-", "-", "-"],
              ["-", "-", "-"]]
show()

while True:
    # player1
    print("PLAYER 1")
    while True:
        row = int(input("enter row: "))
        col = int(input("enter col: "))
        if 0 <= row <= 2 and 0 <= col <= 2 :
            if game_board[row][col] == "-":
                game_board[row][col] = "X"
                show()
                check_game()
                break
            else:
                print("yek khane digar")
        else:
            print("beyne 0 va 2")        

    #player 2
    print("PLAYER 2")
    while True:
        row = int(input("enter row: "))
        col = int(input("enter col: "))
        if 0 <= row <= 2 and 0 <= col <= 2 :
            if game_board[row][col] == "-":
                game_board[row][col] = "O"
                show()
                check_game()
                break
            else:
                print("yek khane digar")
        else:
            print("beyne 0 va 2")  
    
    