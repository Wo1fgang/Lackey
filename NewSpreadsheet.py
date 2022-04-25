import pyautogui
import time
import os

pyautogui.PAUSE = 0.5

project_folder = os.getcwd()


def CrtNewSpreadsheet():
    if (pyautogui.locateOnScreen(f'{project_folder}/Pattern/NewSpreadsheet.png', confidence=0.9,
                                 grayscale=True)) is None:
        pyautogui.click(
            pyautogui.locateOnScreen(f'{project_folder}/Pattern/MainMenu.png', confidence=0.9,
                                     grayscale=True))
        pyautogui.click(pyautogui.locateOnScreen(f'{project_folder}/Pattern/NewSpreadsheet.png', confidence=0.9,
                                                 grayscale=True))
    else:
        pyautogui.click(
            pyautogui.locateOnScreen(f'{project_folder}/Pattern/NewSpreadsheet.png', confidence=0.9,
                                     grayscale=True))
    time.sleep(4)


if __name__ == "__main__":
    CrtNewSpreadsheet()