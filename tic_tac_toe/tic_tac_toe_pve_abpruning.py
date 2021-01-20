import math     # for the infinite constant
import copy     # for duplicating arrays
import random
from tic_tac_toe_pvp import *

# # count = 0
playerLetter = "O"
opponentLetter = "X"

# # using list comprehension to create board with dimensions of width and height
# board = [[" " for x in range(width)] for y in range(height)]
# board = [
#     ["X", "X", "O"],
#     ["X", "O", "X"],
#     [" ", " ", " "],
# ]                       # initializing the board (hard code)


def selectRandom(board):
    spacesEmpty = getSpacesEmpty(board)
    insertLetter(board, opponentLetter, random.choice(spacesEmpty))



def minimax(letter, board, depth, alpha, beta, isMaximizer):
    # global count
    # reminder alpha is the highest value of branches from the same node and depth
    # reminder beta is the lowest value of branches from the same branches and depth
    # calculating the rating of how much 
    # count += 1
    # checking to see if the game should continue
    if isWinner(board, playerLetter):       # if the player has won
        return -10 + depth
    elif isWinner(board, opponentLetter):   # if the computer has won
        return 10 - depth
    elif isBoardFull(board):                # if the board is full
        return 0    

    # checks if it is the player's turn
    if isMaximizer:
        # optimal choice for computer
        maxEval = -math.inf
        # iterating through each empty space
        for i in getSpacesEmpty(board):
            # copies the board
            boardCopy = copy.deepcopy(board)
            # inserts the theoretical letter into the board copy
            insertLetter(boardCopy, letter, i)
            # calls itself to determine possibilities in further turns
            eval = minimax(playerLetter, boardCopy, depth + 1, alpha, beta, False)
            # if there is a more computer optimal choice
            if (eval > maxEval):
                maxEval = eval
                bestMove = i
            # setting the alpha value to the highest value (from other branches) the maximizing node will choose
            alpha = max(alpha, eval)
            # if there is another value lower than the highest value (minimizing node will prioritize the lower value)
            if beta <= alpha:
                break
        # once the function returns to the top of the tree
        if depth == 0:
            # return the most optimal computer move of the tree
            return bestMove
        # return the most optimal computer move in this branch
        return maxEval
    else:
        # optimal choice for the player
        minEval = math.inf
        # iterating through each empty space
        for i in getSpacesEmpty(board):
            # copies the board
            boardCopy = copy.deepcopy(board)
            # inserts the theoretical letter into the board copy
            insertLetter(boardCopy, letter, i)
            # calls itself to determine possibilities in further turns
            eval = minimax(opponentLetter, boardCopy, depth + 1, alpha, beta, True)
            # picks the more player optimal choice
            minEval = min(eval, minEval)
            # setting the beta value to the lowest value (from other branches) the minimizing node will choose                                 
            beta = min(beta, eval)
            # if there is another value higher than the lowest value (maximizing node will prioritize the higher value)
            if beta <= alpha:
                break
        # returns the most player optimal choice
        return minEval


def compMove(board):
    # global count
    move = minimax(opponentLetter, board, 0, -math.inf, math.inf, True)
    # print("Computer searched through " + str(count))
    # count = 0
    return move

# Player vs Easy Computer (Environment)
def pveEasy(board):
    playerFirstTurn = True if input("Do you want to go first (y/n): ") == "y" else False
    global playerLetter 
    global opponentLetter

    if playerFirstTurn: 
        playerLetter = "X"
        opponentLetter = "O"
        # player gets to move
        playerMove(board, playerLetter)
        # displays the board
        printBoard(board)
    else:
        playerLetter = "O"
        opponentLetter = "X"

    # play the game while the board is not full
    while not(isBoardFull(board)):
        # checks if player has won yet
        if not(isWinner(board, playerLetter)):
            # computer places in a random spot
            selectRandom(board)
            # displays the board
            printBoard(board)
        else:
            print(playerLetter + "\'s won this time. NICE!")
            break

        # checking if the board is full
        if (isBoardFull(board)):
            break
        
        # checks if computer has not won yet
        if not(isWinner(board, opponentLetter)):
            # player gets to move
            playerMove(board, playerLetter)
            # displays board
            printBoard(board)
        else:
            print("Sorry, the computer won.")
            break
    
    if isBoardFull(board):
        print("Tie Game!")


# Player vs Impossible Computer (Environment)
def pveImpossible(board):
    playerFirstTurn = True if input("Do you want to go first? (y/n): ") == "y" else False
    global playerLetter 
    global opponentLetter

    if playerFirstTurn: 
        playerLetter = "X"
        opponentLetter = "O"
        # player gets to move
        playerMove(board, playerLetter)
        # displays the board
        printBoard(board)
    else:
        playerLetter = "O"
        opponentLetter = "X"

    # play the game while the board is not full
    while not(isBoardFull(board)):
        # checks if player has won yet
        if not(isWinner(board, playerLetter)):
            # generating the best move for the computer
            move = compMove(board)  
            # if the board became full without anyone winning
            if move != 0:
                # insert letter into optimal space
                insertLetter(board, opponentLetter, move)
                # telling the user where the computer placed their letter
                print("Computer placed an \'" + opponentLetter + "\' in position", move, ":")
                # displaying the board
                printBoard(board)
        else:
            print(playerLetter + "\'s won this time. NICE!")
            break

        # checking if the board is full
        if (isBoardFull(board)):
            break
        
        # checks if computer has not won yet
        if not(isWinner(board, opponentLetter)):
            # player gets to move
            playerMove(board, playerLetter)
            # displays board
            printBoard(board)
        else:
            print("Sorry, the computer won.")
            break
    
    if isBoardFull(board):
        print("Tie Game!")

# def pvp(board):
#     # play the game while the board is not full
#     while not(isBoardFull(board)):
#         # if player O has not won yet
#         if not(isWinner(board, "O")):
#             # player X gets to move
#             playerMove("X")
#             # displays board
#             printBoard(board)
#         else:
#             print("O\'s won this time.")
#             break
        
#         # checking if the board is full
#         if (isBoardFull(board)):
#             break

#         # if player X has not won yet
#         if not(isWinner(board, "X")):
#             # player O gets to move
#             playerMove("O")
#             # displays board
#             printBoard(board)
#         else:
#             print("X\'s won this time.")
#             break
    

#     if isBoardFull(board):
#         print("Tie Game!")

# def main():
#     print("Welcome to Tic-Tac-Toe!")    # introductory message
#     print("There are 3 modes to choose from\na. 2 Player\nb. Easy Computer\nc. Impossible Computer")
#     mode = input("What mode would you like to play?: ")       # user will enter a letter for their choice
#     printBoard()
#     if mode == "1":
#         pvp()
#     elif mode == "2":
#         pveImpossible()


# run the main program
# main()

