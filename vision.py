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

rgb_2_tile: dict[tuple[int, int, int], str] = {
    (255, 157, 95): "L",
    (176, 212, 118): "S",
    # green (194,255,95)???
    (236, 111, 223): "T",
    (255, 226, 95): "O",
    (94, 255, 197): "I",
    (132, 111, 236): "J",
    (255, 97, 105): "Z",
}

rgbs = {
    (255, 157, 95),
    (176, 212, 118),
    (236, 111, 223),
    (255, 226, 95),
    (94, 255, 197),
    (132, 111, 236),
    (255, 97, 105),
}


def get_state(debug=False):
    # raw pixels
    board_image = screen.grab(board_area)

    for i, row in enumerate(ROWS):
        for j, column in enumerate(COLUMNS):
            board[i][j] = 1 if board_image.pixel(column, row) != (0, 0, 0) else 0

    tile_image = screen.grab(tile_area)
    pixel = tile_image.pixel(0, 0)
    tetromino = ""
    if pixel in rgbs:
        tetromino = rgb_2_tile[pixel]

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
