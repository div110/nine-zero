import pyautogui


def rotate(rotation: int) -> None:

    if rotation == 1:
        pyautogui.write("d")
    elif rotation == 2:
        pyautogui.write("w")
    elif rotation == 3:
        pyautogui.write("a")

    return


def slide(index_l: int) -> None:
    pyautogui.write("jjjjjj")

    pyautogui.write(index_l * "l")
    pyautogui.write("i")

    return


def place(index_l: int, rotation: int) -> None:
    print("at: ", index_l, "rotated: ", rotation)
    print(10 * "-")
    rotate(rotation)
    slide(index_l)
    return


if __name__ == "__main__":
    pass
