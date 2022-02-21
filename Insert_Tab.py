import pyautogui

pyautogui.PAUSE = 0.5


def InsertTab():
    pyautogui.click(pyautogui.locateOnScreen('Pattern\\Insert.png', confidence=0.9, grayscale=True))  # Click on Insert


if __name__ == "__main__":
    InsertTab()
