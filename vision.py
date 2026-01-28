import pyautogui, time

COLUMNS = [542, 574, 605, 637, 668, 700, 731, 763, 794, 826]
ROWS = [
    122,
    153,
    185,
    216,
    248,
    279,
    311,
    342,
    374,
    405,
    437,
    468,
    500,
    531,
    563,
    594,
    626,
    657,
    689,
]

# 31/32 horizontal
# 31/32 vertical
board: list[list[bool]] = [[False for _ in range(10)] for _ in range(20)]

while True:
    board = [[False for _ in range(10)] for _ in range(20)]

    screen = pyautogui.screenshot()

    for i, x in enumerate(COLUMNS):
        for j, y in enumerate(ROWS):
            rgb = screen.getpixel((x, y))

            if rgb != (0, 0, 0, 255):
                print(rgb)
                board[j][i] = True

    for row in board:
        print(row)
