import pyautogui
import time
import os
import c
import GoFullscreen

GoFullscreen.goFullScreen()

pyautogui.PAUSE = 0.5

project_folder = os.getcwd()



def CrtNewDoc():
    if (pyautogui.locateOnScreen(f'{project_folder}/Pattern/NewDocument.png', confidence=0.9)) is None:
        c.click('MainMenu')
        c.click('NewDocument')
    else:
        c.click('NewDocument')
    time.sleep(4)

if __name__ == "__main__":
    CrtNewDoc()
