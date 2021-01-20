# declaring the values for the board's width and height
width, height = 3, 3

playerLetter = "X"
opponentLetter = "O"

# This method is for displaying the current state of the board
def printBoard(board):
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
def isSpaceEmpty(board, pos):
    row = (pos - 1) // 3               # calculates row number
    col = (pos - 1) % 3         # calculates col number
    return board[row][col] == " "   # returning boolean value 


def playerMove(board, letter):
    run = True          # used to continue the while loop
    while run:          # while the user does not enter a valid input
        # prompting the user for their input
        move = input("What position would you like to place an \'" + letter + "\'? (1-9): ")
        try:
            # attempts to convert the input to an integer
            move = int(move)
            # checks if the move is in the position range
            if move > 0 and move < 10:
                # checks if the position they chose is empty
                if isSpaceEmpty(board, move):
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

def pvp(board):
    # play the game while the board is not full
    while not(isBoardFull(board)):
        # if player O has not won yet
        if not(isWinner(board, opponentLetter)):
            # player X gets to move
            playerMove(board, playerLetter)
            # displays board
            printBoard(board)
        else:
            print(opponentLetter + "\'s won this time.")
            break
        
        # checking if the board is full
        if (isBoardFull(board)):
            break

        # if player X has not won yet
        if not(isWinner(board, playerLetter)):
            # player O gets to move
            playerMove(board, opponentLetter)
            # displays board
            printBoard(board)
        else:
            print(playerLetter + "\'s won this time.")
            break
    

    if isBoardFull(board):
        print("Tie Game!")

# def main():
#     print("Welcome to Tic-Tac-Toe!")    # introductory message
#     printBoard()
#     pvp()

# player1 = "X"
# player2 = "O"
# main()