import os
import pyautogui

pyautogui.PAUSE = 0.5

project_folder = os.getcwd()


def InsertTab():
    if (pyautogui.locateOnScreen(f'{project_folder}/Pattern/Insert.png', confidence=0.9, grayscale=True)) is None:
        pyautogui.click(pyautogui.locateOnScreen(f'{project_folder}/Pattern/Insert2.png', confidence=0.9, grayscale=True))
    else:
        pyautogui.click(pyautogui.locateOnScreen(f'{project_folder}/Pattern/Insert.png', confidence=0.9, grayscale=True))


if __name__ == "__main__":
    InsertTab()
