import pyautogui
import time

pyautogui.PAUSE = 0.5

def CrtNewDoc():
    if (pyautogui.locateOnScreen('Pattern\\NewDocument.png', confidence=0.9,
                                 grayscale=True)) is None:
        pyautogui.click(
            pyautogui.locateOnScreen('Pattern\\MainMenu.png', confidence=0.9,
                                     grayscale=True))
        pyautogui.click(pyautogui.locateOnScreen('Pattern\\NewDocument.png', confidence=0.9,
                                                 grayscale=True))
    else:
        pyautogui.click(
            pyautogui.locateOnScreen('Pattern\\NewDocument.png', confidence=0.9,
                                     grayscale=True))
    time.sleep(4)


if __name__ == "__main__":
    CrtNewDoc()
