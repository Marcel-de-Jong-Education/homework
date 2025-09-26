import numpy as np

board = np.array(
    [
    ["X", "O", "X"],
    [" ", "X", "O"],
    ["O", " ", "X"]
    ]
    )

for row in board:
    print(" | ".join(row))
    print("-" * 9)
