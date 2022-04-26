import pyautogui
import os
import Buttons
import pyperclip
import time
from datetime import datetime
import NewDocument
import c
import csv
import GoFullscreen

# os.startfile("C:\\Program Files\\ONLYOFFICE\\DesktopEditors\\DesktopEditors.exe") # Launching DesktopEditor
# time.sleep(8)

test = os.path.basename(__file__)

project_folder = os.getcwd()

pyautogui.PAUSE = 0.5

GoFullscreen.goFullScreen()

# Changing username
if pyautogui.locateOnScreen(f'{project_folder}/Pattern/Settings.png', confidence=0.9, grayscale=True) is None:
    c.click('MainMenu')
    c.click('Settings')
Buttons.tab()
pyperclip.copy('Some text to check if changing username works')
pyautogui.hotkey('Ctrl', 'v')
pyautogui.click(pyautogui.locateOnScreen(f'{project_folder}/Pattern/Apply.png', confidence=0.9, grayscale=True))

date = datetime.now().strftime("%d.%m.%Y %H.%M.%S")  # date = Current date in "d.m.Y H.M.S" format

if (pyautogui.locateOnScreen(f'{project_folder}/Pattern/ChangedUsername.png', confidence=0.9, grayscale=True)) is None:
    with open('Completed Tests.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ')
        writer.writerow([f"{date}', {test}, FAILED"])
    print("There's a problem with changing username \n")
else:
    with open('Completed Tests.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ')
        writer.writerow([f"{date}, {test}, SUCCESS"])

c.click('ResetToDefault')
c.click('Apply')