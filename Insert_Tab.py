import pyautogui
import os.path

pyautogui.PAUSE = 0.5

os.chdir('C:\\Auto')


def InsertTab():
    pyautogui.click(pyautogui.locateOnScreen('Insert.png', confidence=0.9, grayscale=True))  # Click on Insert


if __name__ == "__main__":
    InsertTab()