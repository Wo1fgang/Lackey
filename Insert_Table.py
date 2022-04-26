import pyautogui
import time
from datetime import datetime  # Library used to get current time
import Buttons  # Importing Buttons.py to quickly use necessary buttonpresses
import os
import c
import csv
import GoFullscreen

pyautogui.PAUSE = 0.5

time.sleep(2)

project_folder = os.getcwd()

test = os.path.basename(__file__)

GoFullscreen.goFullScreen()

def Insert_Table():  # defining function so we can import it into Everything.py
    # pyautogui.click(pyautogui.locateOnScreen('Pattern\\Insert.png', confidence=0.9, grayscale=True))  # Click on "Insert" tab
    # # INSERTING 9x9 TABLE
    if pyautogui.click(pyautogui.locateOnScreen(f'{project_folder}/Pattern/Insert.png', confidence=0.9)) is None:
        c.click('Insert2')
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
        pyautogui.screenshot(f'{project_folder}/Completed Tests/Failed/Table/{date}.png')
        with open('Completed Tests.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=' ')
            writer.writerow([f"{date}', {test}, FAILED"])
        print("There's a problem with inserting 9x9 table")
    else:
        pyautogui.screenshot(f'{project_folder}/Completed Tests/Success/Image/URL/{date}.png')
        with open('Completed Tests.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=' ')
            writer.writerow([f"{date}, {test}, SUCCESS"])


if __name__ == "__main__":
    Insert_Table()