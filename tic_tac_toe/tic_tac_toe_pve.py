import math     # for the infinite constant
import copy     # for duplicating arrays
import random

# declaring the values for the board's width and height
width, height = 3, 3
count = 0
playerLetter = "X"
opponentLetter = "O"

# using list comprehension to create board with dimensions of width and height
board = [[" " for x in range(width)] for y in range(height)]
# board = [
#     ["X", "X", "O"],
#     ["X", "O", "X"],
#     [" ", " ", " "],
# ]                       # initializing the board (hard code)

# This method is for displaying the current state of the board
def printBoard():
    print("-------------------")                # printing the top of the grid
    for i in range(width):                      # iterating through each row
        print("|  ", end="")                    # printing the left wall
        print("  |  ".join(board[i]), end="")   # printing the content of the board
        print("  |")                            # printing the right wall
        print("-------------------")            # printing a breakline

# method for inserting move
def insertLetter(board, letter, pos):      
    row = (pos - 1) // 3        # calculates row number
    col = (pos - 1) % 3         # calculates col number
    board[row][col] = letter

# method for checking if board is full
def isBoardFull(board):                      
    for row in range(height):            # iterating through each row
        for col in range(width):       # iterating through each column
            if board[row][col] == " ":   # if board space is empty
                return False
    return True


# counts number of empty spaces in the board
def countSpacesEmpty(board):
    # initialize counter for empty spaces
    spacesEmpty = 0
    for row in range(height):               # iterating through each row
        for col in range(width):            # iterating through each column
            if board[row][col] == " ":      # if the space is empty
                spacesEmpty += 1
    return spacesEmpty

# gets the positions of empty spaces
def getSpacesEmpty(board):
    spacesEmpty = []
    for row in range(height):               # iterating through each row
        for col in range(width):            # iterating through each column
            if board[row][col] == " ":      # if the space is empty
                spacesEmpty.append(row * 3 + col + 1)   # finds the position number of this space
    return spacesEmpty


# method for checking if space is empty
def isSpaceEmpty(pos):
    row = (pos - 1) // 3               # calculates row number
    col = (pos - 1) % 3         # calculates col number
    return board[row][col] == " "   # returning boolean value 


def playerMove(letter):
    run = True          # used to continue the while loop
    while run:          # while the user does not enter a valid input
        # prompting the user for their input
        move = input("What position would you like to place an \'" + playerLetter + "\'? (1-9): ")
        try:
            # attempts to convert the input to an integer
            move = int(move)
            # checks if the move is in the position range
            if move > 0 and move < 10:
                # checks if the position they chose is empty
                if isSpaceEmpty(move):
                    # breaks the loop
                    run = False
                    # inserts the letter into the board
                    insertLetter(board, letter, move)
                else:
                    print("Space is occupied. Please enter another move.")
            else:
                # tells the user their input is not in the range
                print("Please select a valid position.")

        except:
            # tells the user the input is not a number
            print("Please type a number")


def isWinner(board, letter):
    # checking each column for a win
    for col in range(width):
        if all([True if board[row][col] == letter else False for row in range(height)]):
            return True
    # checking each row for a win
    for row in range(height):
        if all([True if board[row][col] == letter else False for col in range(width)]):
            return True
    # checking top left to bottom right diagonal for win
    if all([True if board[x][x] == letter else False for x in range(width)]):
        return True
    # checking top right to bottom left diagonal for win
    if all([True if board[x][len(board[x])-1-x] == letter else False for x in range(width)]):
        return True
    return False


def selectRandom():
    pass


def minimax(letter, board, depth, isMaximizer):
    global count
    # count += 1
    # calculating the rating of how much this move helps the computer
    # checking to see if the game should continue
    if isWinner(board, playerLetter):       # if the player has won
        count += 1
        return -10 + depth
    elif isWinner(board, opponentLetter):   # if the computer has won
        count += 1
        return 10 - depth
    elif isBoardFull(board):                # if the board is full
        count += 1
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
            eval = minimax(playerLetter, boardCopy, depth + 1, False)
            # if there is a more computer optimal choice
            if (eval > maxEval):
                maxEval = eval
                bestMove = i
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
            eval = minimax(opponentLetter, boardCopy, depth + 1, True)
            # picks the more player optimal choice
            minEval = min(eval, minEval)
        # returns the most player optimal choice
        return minEval


def compMove():
    global count
    move = minimax(opponentLetter, board, 0, True)
    print("Computer searched through " + str(count))
    count = 0
    return move

def main():
    print("Welcome to Tic-Tac-Toe!")    # introductory message
    printBoard()
    playerFirstTurn = True if input("Do you want to go first? (y/n): ") == "y" else False

    # if the player wants to go first
    if playerFirstTurn: 
        # player gets to move
        playerMove(playerLetter)
        # displays the board
        printBoard()

    # play the game while the board is not full
    while not(isBoardFull(board)):
        # checks if player has won yet
        if not(isWinner(board, playerLetter)):
            # generating the best move for the computer
            move = compMove()
            # if the board became full without anyone winning
            if move == 0:
                print("Tie game?")
            else:
                # insert letter into optimal space
                insertLetter(board, opponentLetter, move)
                # telling the user where the computer placed their letter
                print("Computer placed an \'" + opponentLetter + "\' in position", move, ":")
                # displaying the board
                printBoard()
        else:
            print(playerLetter + "\'s won this time. NICE!")
            break

        # checking if the board is full
        if (isBoardFull(board)):
            break
        
        # checks if computer has not won yet
        if not(isWinner(board, opponentLetter)):
            # player gets to move
            playerMove(playerLetter)
            # displays board
            printBoard()
        else:
            print("Sorry, O\'s won.")
            break
    
    if isBoardFull(board):
        print("Tie Game!")


# run the main program
main()

