import pyautogui
import os

import c

project_folder = os.getcwd()

pyautogui.PAUSE = 0.8


def ChangeThemeToLight():
    if pyautogui.locateOnScreen(f'{project_folder}/Pattern/MainMenu.png', confidence=0.9) is None:
        pyautogui.click(pyautogui.locateOnScreen(f'{project_folder}/Pattern/MainMenuDark.png', confidence=0.9))
        c.click("SettingsDark")
        for _ in range(5):
            pyautogui.press('Tab')
        pyautogui.press('Down')
        pyautogui.press('Enter')
        for _ in range(2):
            pyautogui.press('Tab')
        if os.name == "nt":
            pyautogui.press('Tab')
        pyautogui.press('Enter')
