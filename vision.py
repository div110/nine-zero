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
# on 1366x76
board_area = {"top": 122, "left": 542, "width": 283, "height": 598}
tile_area = {"top": 100, "left": 668, "width": 1, "height": 1}

board = [[0 for _ in range(10)] for _ in range(20)]


rgbs = {
    (255, 157, 95),  # L(249, 136, 68)
    (176, 212, 118),  # S 178, 246, 67
    (236, 111, 223),  # T
    (255, 226, 95),  # O
    (94, 255, 197),  # I
    (132, 111, 236),  # J(109, 84, 224)
    (255, 97, 105),  # Z
}


def get_tile(rgb: tuple[int, int, int]) -> str:
    r, g, b = rgb

    if r > 200 and b > 200:
        return "T"

    elif r > 200 and g > 200:
        return "O"

    elif r > 100 and g > 50 and b > 200:
        return "J"

    elif r > 200 and g > 127:
        return "L"

    elif r > 150 and g > 200:
        return "S"

    elif g > 200:
        return "I"

    elif r > 200 and g < 140 and b < 140:
        return "Z"

    return ""


def get_state(debug=True):
    # raw pixels
    board_image = screen.grab(board_area)

    for i, row in enumerate(ROWS):
        for j, column in enumerate(COLUMNS):
            board[i][j] = 1 if board_image.pixel(column, row) != (0, 0, 0) else 0

    tile_image = screen.grab(tile_area)
    pixel = tile_image.pixel(0, 0)

    print(pixel)
    tetromino = get_tile(pixel)
    print(tetromino)

    if debug:
        image = Image.frombytes("RGB", tile_image.size, tile_image.bgra, "raw", "BGRX")
        image.save("screen_objects/tile.png")

        image = Image.frombytes(
            "RGB", board_image.size, board_image.bgra, "raw", "BGRX"
        )
        image.save("screen_objects/area.png")

    return (board, tetromino)


if __name__ == "__main__":
    get_state()
