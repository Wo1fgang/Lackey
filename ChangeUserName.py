import pyautogui
import os
import Buttons
import pyperclip
import time
from datetime import datetime
import NewDocument
import clicker
import csv
import GoFullscreen

test = os.path.basename(__file__)

project_folder = os.getcwd()

pyautogui.PAUSE = 0.5

GoFullscreen.goFullScreen()


def CheckUsername():
    # Changing username
    if pyautogui.locateOnScreen(f'{project_folder}/Pattern/Settings.png', confidence=0.9, grayscale=True) is None:
        clicker.click('MainMenu')
    clicker.click('Settings')
    Buttons.tab()
    pyperclip.copy('Some text to check if changing username works')
    pyautogui.hotkey('Ctrl', 'v')
    pyautogui.click(pyautogui.locateOnScreen(f'{project_folder}/Pattern/Apply.png', confidence=0.9, grayscale=True))

    date = datetime.now().strftime("%d.%m.%Y %H.%M.%S")  # date = Current date in "d.m.Y H.M.S" format

    if (pyautogui.locateOnScreen(f'{project_folder}/Pattern/ChangedUsername.png', confidence=0.9, grayscale=True)) is None:
        with open('Completed Tests.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=' ')
            writer.writerow([f"{date}', {test}, FAILED"])
        print(f"{date}', {test}, FAILED")
    else:
        with open('Completed Tests.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=' ')
            writer.writerow([f"{date}, {test}, SUCCESS"])
        print(f"{date}, {test}, SUCCESS")

    clicker.click('ResetToDefault')
    clicker.click('Apply')


if __name__ == "__main__":  # Fail-safe so that this script would not run when we import in into Everything.py
    CheckUsername()
