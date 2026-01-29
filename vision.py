import mss
from PIL import Image

COLUMNS = [0, 32, 63, 95, 126, 158, 189, 221, 252, 282]
ROWS = [
    0,
    31,
    63,
    94,
    126,
    157,
    189,
    220,
    252,
    283,
    315,
    341,
    373,
    404,
    436,
    467,
    499,
    530,
    562,
    592,
]

# 31/32 horizontal
# 31/32 vertical

screen = mss.mss()

board_area = {"top": 122, "left": 542, "width": 283, "height": 598}
board = [[0 for _ in range(10)] for _ in range(20)]


def get_state(debug=False):
    # raw pixels
    screen_image = screen.grab(board_area)

    for i, row in enumerate(ROWS):
        for j, column in enumerate(COLUMNS):
            board[i][j] = 1 if screen_image.pixel(column, row) != (0, 0, 0) else 0

    if debug:
        image = Image.frombytes(
            "RGB", screen_image.size, screen_image.bgra, "raw", "BGRX"
        )
        image.save("area.png")

    print(1)
    return board


if __name__ == "__main__":
    get_state()
