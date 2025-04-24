from scripts.txt_prep import preparation
from scripts._solver import solve
import numpy as np

def print_board(board):
    for row in board:
        print(" ".join(str(x) for x in row))

if __name__ == "__main__":
    path = "data/sudoku_9x9_40_empty.txt"
    length = 9
    try:
        board = preparation(path,9)

        size = board.shape[0]
        if size > 16:
            print("Size is too large. Only 4x4, 9x9, and 16x16 are supported.")
        else:
            print("Initial Sudoku:\n")
            print_board(board)

            if solve(board, size):
                print("\nSolved Sudoku:\n")
                print_board(board)
            else:
                print("\nNo solution exists.")
    except Exception as e:
        print(f"Error: {e}")
