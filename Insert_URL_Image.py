import pyautogui
import pyperclip
from datetime import datetime
import Buttons
import time
import os
import c
import csv
import sys
import GoFullscreen

test = os.path.basename(__file__)

pyautogui.PAUSE = 0.8

project_folder = os.getcwd()

# CrtNewDoc()
time.sleep(1)

GoFullscreen.goFullScreen()


def Insert_URL_Image():
    if pyautogui.click(pyautogui.locateOnScreen(f'{project_folder}/Pattern/Insert.png', confidence=0.9)) is None:
        c.click('Insert2')
    pyautogui.press('alt')
    pyautogui.press('i')
    pyautogui.press('e')
    Buttons.down()
    Buttons.down()  # Choosing insert from URL
    Buttons.enter()  # OK
    pyperclip.copy('https://i.redd.it/or438ov4zno81.jpg')
    pyautogui.hotkey('Ctrl', 'v')  # Insert Image URL
    Buttons.enter()
    if (pyautogui.locateOnScreen(f'{project_folder}/Pattern/ErrorURL.png', confidence=0.8)) is not None:
        pyautogui.press('Escape')  # Escape from active image
        print("something is wrong with clipboard, couldn't paste URL")
        sys.exit()
    Buttons.escape()
    Buttons.right()
    Buttons.enter()  # Next Line

    date = datetime.now().strftime("%d.%m.%Y %H.%M.%S")

    if (pyautogui.locateOnScreen(f'{project_folder}/Pattern/InsertedURLImage.png', confidence=0.9, grayscale=True)) is None:
        pyautogui.screenshot(f'{project_folder}/Completed Tests/Failed/Image/URL/{date}.png')
        with open('Completed Tests.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=' ')
            writer.writerow([f"{date}', {test}, FAILED"])
        print("There's a problem with inserting image from URL")
    else:
        with open('Completed Tests.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=' ')
            writer.writerow([f"{date}, {test}, SUCCESS"])


if __name__ == "__main__":
    Insert_URL_Image()