import sys

board = [["-","-","-"],
        ["-","-","-"],
        ["-","-","-"]]

def displayBoard():
    boardText = '\n---------\n'.join([' | '.join(x) for x in board])
    print(boardText)


def changeBoard(player,x,y):
    if x not in ["1","2", "3"]: return [False, "ERROR: Enter Valid X value"]
    if y not in ["1","2", "3"]: return [False, "ERROR: Enter Valid Y value"]
    x = int(x)
    y = int(y)
    if board[y-1][x-1] != "-": return [False, "Cell is taken"]
    key = 'X' if player == 1 else 'O'
    board[y-1][x-1] = key
    return [True, f"Changed value to {key}"]

def checkWin():
    # horizontal
    for x in board:
        if len(set(x)) == 1 and set(x).pop() != "-":
            return x[0]
    # vertical
    for x in range(3):
        temp = [board[y][x] for y in range(3)]
        if len(set(temp)) == 1 and set(temp).pop() != "-":
            return temp[0]

    # diagonal top left to bottom right
    temp = [board[0][0],board[1][1],board[2][2]]
    if len(set(temp)) == 1 and set(temp).pop() != "-":
        return temp[0]

    # diagonal top right to bottom left
    temp = [board[0][2],board[1][1],board[2][0]]
    if len(set(temp)) == 1 and set(temp).pop() != "-":
        return temp[0]
    
    return None

def checkDraw():
    temp = [board[y][x] for x in range(3) for y in range(3)]
    if "-" not in temp:
        print("DRAW!")
        displayBoard()
        print("Thank you for playing!")
        sys.exit(0)
        
if __name__== "__main__" :
    print("Hi! Welcome to tic tac toe")

    currentPlayer = 1

    while(True):

        checkDraw()

        print("""\nChoose one of the options below:
        1 - display board
        2 - print current player
        3 - play
        exit - closes the game
        """)
        option = input("enter option: ")
        print("")

        if option == "1":
            print("Here is the current board:\n")
            displayBoard()
        elif option == "2":
            print(f"Current player: {currentPlayer}")
        elif option == "3":
            while(True):
                x = input("enter x coordinate (1 to 3): ")
                y = input("enter y coordinate (1 to 3): ")
                res = changeBoard(currentPlayer,x,y)
                print(res[1])
                if res[0]:
                    if(checkWin()!=None):
                        print(f"WINNER IS: PLAYER {currentPlayer}")
                        displayBoard()
                        print("Thank you for playing!")
                        sys.exit(0)
                    currentPlayer = 2 if currentPlayer==1 else 1
                    print("Change player")
                    break

        elif option == "exit":
            print("Thank you for playing!")
            sys.exit(0)
        else:
            print("Please choose a valid option")