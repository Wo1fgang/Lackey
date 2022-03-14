import pyautogui

pyautogui.PAUSE = 0.5


def InsertTab():
    if (pyautogui.locateOnScreen('Pattern\\Insert.png', confidence=0.9, grayscale=True)) is None:
        pyautogui.click(pyautogui.locateOnScreen('Pattern\\Insert2.png', confidence=0.9, grayscale=True))
    else:
        pyautogui.click(pyautogui.locateOnScreen('Pattern\\Insert.png', confidence=0.9, grayscale=True))


if __name__ == "__main__":
    InsertTab()
