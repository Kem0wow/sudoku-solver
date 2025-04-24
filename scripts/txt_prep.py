import numpy as np

def preparation(path, length):
    board = []
    with open(path, "r") as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) != length:
                raise Exception(f"Line length mismatch in file '{path}'")
            row = [int(x) if x != '.' else 0 for x in parts]
            board.append(row)

    if len(board) != length:
        raise Exception(f"Row count mismatch in file '{path}'")

    return np.array(board)
