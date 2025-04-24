def is_valid(board, row, col, num, size):
    for i in range(size):
        if board[row][i] == num or board[i][col] == num:
            return False
    
    box_size = int(size**0.5)
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
