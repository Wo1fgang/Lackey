import pyautogui
import time
import os
import clicker
import GoFullscreen
import Change_Theme

Change_Theme.ChangeThemeToLight()

GoFullscreen.goFullScreen()

pyautogui.PAUSE = 0.5

project_folder = os.getcwd()


def CrtNewPresentation():
    if (pyautogui.locateOnScreen(f'{project_folder}/Pattern/NewSpreadsheet.png', confidence=0.9)) is None:
        clicker.click('MainMenu')
        clicker.click('NewPresentation')
    else:
        clicker.click('NewPresentation')
    time.sleep(4)


if __name__ == "__main__":
    CrtNewPresentation()