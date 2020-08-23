board = [["-","-","-"],
        ["-","-","-"],
        ["-","-","-"]]

def display_board():
    boardText = '\n---------\n'.join([' | '.join(x) for x in board])
    return boardText


def changeBoard(player,x,y):
    if x not in ["1","2", "3"]: return "ERROR: Enter Valid X value"
    if y not in ["1","2", "3"]: return "ERROR: Enter Valid Y value"
    x = int(x)
    y = int(y)
    if board[y-1][x-1] != "-": return "Cell is taken"
    key = 'X' if player == 1 else 'O'
    board[y-1][x-1] = key
    return f"Changed value to {key}"

if __name__== "__main__" :
    print("Hi! Welcome to tic tac toe")

    currentPlayer = 1

    while(True):
        print("""\nChoose one of the options below:
        1 - display board
        2 - print current player
        3 - play
        exit - closes the game
        """)
        option = input("enter option: ")
        print("\n")
        if option == "1":
            print("Here is the current board:\n")
            print(display_board())
        elif option == "2":
            print(f"Current player: {currentPlayer}")
        elif option == "3":
            x = input("enter x coordinate (1 to 3): ")
            y = input("enter y coordinate (1 to 3): ")
            print(changeBoard(currentPlayer,x,y))

        elif option == "exit":
            print("Thank you for playing!")
            break
        else:
            print("Please choose a valid option")



# board
# display board
# play game
# handle turn
# check win
    # check rows
    # check columns
    # check diagonals
# check tie
# flip player