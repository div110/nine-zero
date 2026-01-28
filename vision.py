import pyautogui, mss

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

screen = mss.mss()

board_area = {"top": 122, "left": 542, "width": 283, "height": 598}
