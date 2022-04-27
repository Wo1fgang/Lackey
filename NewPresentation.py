import pyautogui
import time
import os
import c
import GoFullscreen
import Change_Theme

Change_Theme.ChangeThemeToLight()

GoFullscreen.goFullScreen()

pyautogui.PAUSE = 0.5

project_folder = os.getcwd()


def CrtNewPresentation():
    if (pyautogui.locateOnScreen(f'{project_folder}/Pattern/NewSpreadsheet.png', confidence=0.9)) is None:
        c.click('MainMenu')
        c.click('NewPresentation')
    else:
        c.click('NewPresentation')
    time.sleep(4)


if __name__ == "__main__":
    CrtNewPresentation()