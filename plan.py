from vision import get_state
from putter import place
import pyautogui
import time

# describing possible terrain differences
shape_dict = {
    "I": [[0, 0, 0]],
    "J": [[2], [0, -1], [0, 0], [0]],  # dont KNOW
    "L": [[-2], [1, 0], [0, 0], [0]],
    "O": [[0]],
    "S": [[0, 1], [-1]],
    "T": [[-1, 1], [-1], [1], [0, 0]],
    "Z": [[0, -1], [1]],
    "": [],
}

rotation_translation = {
    "I": [0, 1, 1, 1, 1, 1, 1],
    "J": [1, 2, 0, 3],
    "L": [3, 2, 0, 1],
    "O": [0],
    "S": [0, 1],
    "T": [2, 3, 1, 0],
    "Z": [0, 3],
    "": [0],
}


def find_best(terrain: list[int], tile: str) -> tuple[int, int]:
    if not tile:
        return (-1, -1)
    rotations = shape_dict[tile]

    for r, rotation in enumerate(rotations):
        for i in range(11 - len(rotation) - 1):
            delta: list[int] = []
            for j in range(len(rotation)):
                change = terrain[i + j + 1] - terrain[i + j]
                if tile == "I":
                    if change >= 2:
                        return i + j - 1, 1
                    elif change <= -2:
                        return i + j + 1, 1

                delta.append(change)

            if delta == rotation:
                rotate = r
                left_col = i
                print(terrain)
                print("found: ", rotation)
                return left_col, rotate

    return 0, 0


def single_tile():
    board, tile = get_state()
    # 20 rows 10 columns -> board[19][9]

    terrain = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(9, -1, -1):
        for j in range(19, -1, -1):
            if board[j][i] == 1 or (board[j][i] == 0 and board[j - 1][i] == 1):
                terrain[i] += 1
            else:
                break

    minimal = min(terrain)
    for i in range(10):
        terrain[i] -= minimal

    left_col, rotate = find_best(terrain, tile)
    rotate = rotation_translation[tile][rotate]

    if left_col == -1 and rotate == -1:
        return
    place(left_col, rotate)


while True:
    single_tile()
