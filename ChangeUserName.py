import pyautogui
import os
import Buttons
import pyperclip
from datetime import datetime
import clicker
import csv
import GoFullscreen
import Change_Theme

Change_Theme.ChangeThemeToLight()

test = os.path.basename(__file__)

project_folder = os.getcwd()

pyautogui.PAUSE = 0.5

GoFullscreen.goFullScreen()

day_of_test = datetime.now().strftime("%d.%m.%Y %H")

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
        with open(f'{project_folder}/Completed Tests/{day_of_test}.csv', 'a',
                  newline='') as csvfile:  # Open "Completed Tests.csv"
            writer = csv.writer(csvfile, delimiter=' ')
            writer.writerow([f"{date}', {test}, FAILED"])  # Write date, test and result
        print(f"{date}', {test}, FAILED")  # Print to console that something's wrong
    else:  # If everything's alright:
        with open(f'{project_folder}/Completed Tests/{day_of_test}.csv', 'a',
                  newline='') as csvfile:  # Open "Completed Tests.csv"
            writer = csv.writer(csvfile, delimiter=' ')
            writer.writerow([f"{date}, {test}, SUCCESS"])  # Write date, test and result
        print(f"{date}, {test}, SUCCESS")

    clicker.click('ResetToDefault')
    clicker.click('Apply')


if __name__ == "__main__":  # Fail-safe so that this script would not run when we import in into Everything.py
    CheckUsername()
