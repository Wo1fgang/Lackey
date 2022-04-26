import pyautogui
import os

project_folder = os.getcwd()


def goFullScreen():
    if pyautogui.locateOnScreen(f'{project_folder}/Pattern/SmallWindow.png', confidence=0.9) is not None:
        pyautogui.click(pyautogui.locateOnScreen(f'{project_folder}/Pattern/SmallWindow.png', confidence=0.9))