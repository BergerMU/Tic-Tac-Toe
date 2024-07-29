# Tic tac toe game - Berger

import numpy as np
import pandas as pd

def checkWin(board, XorO):
    if board[0,0] == board[1,1] == board[2,2]:
        print(f"{XorO} won!")
        print(board)
        playAgain()
        return True
    elif board[0,2] == board[1,1] == board[2,0]:
        print(f"{XorO} won!")
        print(board)
        playAgain()
        return True
    else:
        for x in range(len(board[0])):
            if board[0,x] == board[1,x] == board[2,x]:
                print(f"{XorO} won!")
                print(board)
                playAgain()
                return True
            elif board[x,0] == board[x,1] == board[x,2]:
                print(f"{XorO} won!")
                print(board)
                playAgain()
                return True
        return False

def placePiece(XorO, board):
    print(f"-------------------------")
    print(board)
    print(f"{XorO}'s Turn")
    try:
        move = int(input("Piece Location: "))
        if move <= 0 or move > 9:
            print("Invalid move, must be between 1-9")
            return placePiece(XorO, board)
        else:
            if move <= 3:
                move -= 1
                if board[0,move] == "X" or board[0,move] == "O":
                    print("Invalid move, spot already occupied")
                    return placePiece(XorO, board)
                else:
                    board[0,move] = XorO
                    return board
            elif move <= 6:
                move -= 4
                if board[1,move] == "X" or board[1, move] == "O":
                    print("Invalid Move, spot already occupied")
                    return placePiece(XorO, board)
                else:
                    board[1,move] = XorO
                    return board
            else:
                move -= 7
                if board[2,move] == "X" or board[2,move] =="O":
                    print("Invalid Move, spot already occupied")
                    return placePiece(XorO, board)
                else:
                    board[2,move] = XorO
                    return board
    except (ValueError, IndexError):
        print("Invalid move, must be between 1-9")
        return placePiece(XorO, board)

def switchVariable(XorO):
    if XorO == "X": return "O"
    else:           return "X"

def getXorO():
    XorO = input("X or O: ").upper()
    if XorO in ["X", "O"]:
        return XorO
    else:
        print("Invalid Input")
        return getXorO()

def playAgain():
    print(f"-------------------------")
    yesorno = input("Play again?\n(Y/N): ").upper()
    if yesorno == "Y":
        return playGame()
    elif yesorno == "N":
        return quit()
    else:
        print("Invalid Input")
        return playAgain()

def playGame():
    XorO = getXorO()
    board = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).astype(str)
    won = False
    for count in range(9):
        if won == False:
            board = placePiece(XorO, board)
            won = checkWin(board, XorO)
            XorO = switchVariable(XorO)
        if count == 8:
            print("Tie")
            playAgain()

#Welcome screen
print(f"Berger's Tic Tac Toe Game")
playGame()