import pyautogui
import time
import os.path
import pyperclip
from datetime import datetime
from NewDocument import CrtNewDoc
from Insert_Tab import InsertTab
import Buttons


def down():
    pyautogui.press('Down')


pyautogui.PAUSE = 0.5

os.chdir('C:\\Auto')

# CrtNewDoc()

InsertTab()

pyautogui.click(pyautogui.locateOnScreen('Chart.png', confidence=0.9, grayscale=True))
Buttons.down()
Buttons.enter()
time.sleep(4)
pyautogui.click(pyautogui.locateOnScreen('SaveAndExit.png', confidence=0.9, grayscale=True))