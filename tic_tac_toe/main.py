import math     # for the infinite constant
import copy     # for duplicating arrays
import random
import tic_tac_toe_pve_abpruning as tttpve
width, height = 3, 3


def main():
    response = "y"
    while response == "y":
        # using list comprehension to create board with dimensions of width and height
        board = [[" " for x in range(width)] for y in range(height)]
        print("Welcome to Tic-Tac-Toe!")    # introductory message
        print("There are 3 modes to choose from\na. 2 Player\nb. Easy Computer\nc. Impossible Computer")
        mode = input("What mode would you like to play?: ")       # user will enter a letter for their choice
        tttpve.printBoard(board)
        if mode == "1":
            tttpve.pvp(board)
        elif mode == "2": 
            tttpve.pveEasy(board)
        elif mode == "3":
            tttpve.pveImpossible(board)
        else:
            print("Invalid mode. Exiting game.")
            break
        response = input("Do you want to play again? (y/n): ")

if __name__ == "__main__":
    main()