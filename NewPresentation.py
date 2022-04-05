import pyautogui
import time

pyautogui.PAUSE = 0.5


def CrtNewPresentation():
    if (pyautogui.locateOnScreen('Pattern\\NewPresentation.png', confidence=0.9)) is None:
        pyautogui.click(
            pyautogui.locateOnScreen('Pattern\\MainMenu.png', confidence=0.9))
        pyautogui.click(pyautogui.locateOnScreen('Pattern\\NewPresentation.png'))
    else:
        pyautogui.click(
            pyautogui.locateOnScreen('Pattern\\NewPresentation.png', confidence=0.9))
    time.sleep(4)


if __name__ == "__main__":
    CrtNewPresentation()