import pyautogui
import time
from datetime import datetime  # Library used to get current time
import Buttons  # Importing Buttons.py to quickly use necessary buttonpresses
import os
import clicker
import csv
import GoFullscreen
import NewDocument
import Change_Theme

Change_Theme.ChangeThemeToLight()

pyautogui.PAUSE = 0.5

time.sleep(2)

project_folder = os.getcwd()

test = os.path.basename(__file__)

GoFullscreen.goFullScreen()

day_of_test = datetime.now().strftime("%d.%m.%Y %H")

def Insert_Table():  # defining function so we can import it into Everything.py
    NewDocument.CrtNewDoc()
    if pyautogui.click(pyautogui.locateOnScreen(f'{project_folder}/Pattern/Insert.png', confidence=0.9)) is None:
        clicker.click('Insert2')
    pyautogui.press('alt')
    pyautogui.press('i')
    pyautogui.press('d')
    Buttons.down()
    Buttons.enter()
    pyautogui.typewrite("9")  # Number of columns (9)
    Buttons.tab()  # Next field
    pyautogui.typewrite("9")  # Number of rows (9)
    Buttons.enter()  # Press ОК

    i = 1
    while i < 10:  # Moving down the table
        pyautogui.press('Down')
        i += 1
    Buttons.enter()  # Next line

    date = datetime.now().strftime("%d.%m.%Y %H.%M.%S")  # date = Current date in "d.m.Y H.M.S" format

    if (pyautogui.locateOnScreen(f'{project_folder}/Pattern/CreatedTable.png', confidence=0.9, grayscale=True)) is None:
        with open(f'{project_folder}/Completed Tests/{day_of_test}.csv', 'a', newline='') as csvfile:  # Open "Completed Tests.csv"
            writer = csv.writer(csvfile, delimiter=' ')
            writer.writerow([f"{date}', {test}, FAILED"])  # Write date, test and result
        print(f"{date}', {test}, FAILED") # Print to console that something's wrong
    else:  # If everything's alright:
        with open(f'{project_folder}/Completed Tests/{day_of_test}.csv', 'a', newline='') as csvfile:  # Open "Completed Tests.csv"
            writer = csv.writer(csvfile, delimiter=' ')
            writer.writerow([f"{date}, {test}, SUCCESS"])  # Write date, test and result
        print(f"{date}, {test}, SUCCESS")

    pyautogui.hotkey('Ctrl', 'w')
    Buttons.tab()
    Buttons.enter()


if __name__ == "__main__":
    Insert_Table()