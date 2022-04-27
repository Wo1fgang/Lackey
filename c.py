import os
import sys

import pyautogui

project_folder = os.getcwd()

p = str

pyautogui.PAUSE = 0.8


def click(p):
    if pyautogui.locateOnScreen(f'{project_folder}/Pattern/{p}.png', confidence=0.9) is None:
        print(f"{p} could not be found")
        sys.exit()
    else:
        pyautogui.click(pyautogui.locateOnScreen(f'{project_folder}/Pattern/{p}.png', confidence=0.9))