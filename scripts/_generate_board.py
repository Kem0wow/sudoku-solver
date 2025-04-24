import random
import numpy as np

def is_valid(board, row, col, num, size):
    box_size = int(size ** 0.5)
    if num in board[row] or num in board[:, col]:
        return False
    start_row, start_col = row - row % box_size, col - col % box_size
    for i in range(box_size):
        for j in range(box_size):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def solve(board, size):
    for row in range(size):
        for col in range(size):
            if board[row][col] == 0:
                for num in range(1, size + 1):
                    if is_valid(board, row, col, num, size):
                        board[row][col] = num
                        if solve(board, size):
                            return True
                        board[row][col] = 0
                return False
    return True

def generate_sudoku(size):
    if size not in [4, 9, 16]:
        raise ValueError("Only sizes 4x4, 9x9, and 16x16 are supported.")
    board = np.zeros((size, size), dtype=int)
    attempts = size
    while attempts > 0:
        row, col = random.randint(0, size-1), random.randint(0, size-1)
        num = random.randint(1, size)
        if board[row][col] == 0 and is_valid(board, row, col, num, size):
            board[row][col] = num
            attempts -= 1
    if not solve(board, size):
        return generate_sudoku(size)
    return board

def remove_cells(board, num_to_remove):
    size = len(board)
    cells = [(i, j) for i in range(size) for j in range(size)]
    random.shuffle(cells)
    for i in range(num_to_remove):
        r, c = cells[i]
        board[r][c] = 0
    return board

def save_sudoku_to_txt(board, filename):
    with open(filename, "w") as f:
        for row in board:
            line = " ".join(str(num) if num != 0 else '.' for num in row)
            f.write(line + "\n")

def generate_and_save(size, empty_cells):
    sudoku = generate_sudoku(size)
    sudoku = remove_cells(sudoku, empty_cells)
    filename = f"sudoku_{size}x{size}_{empty_cells}_empty.txt"
    save_sudoku_to_txt(sudoku, filename)
    print(f"Sudoku saved to: {filename}")

if __name__ == "__main__":
    size = 9
    empty_cells = 40
    generate_and_save(size, empty_cells)