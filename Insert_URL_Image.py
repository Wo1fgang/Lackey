import pyautogui
import pyperclip
from datetime import datetime
import Buttons
import time
import os
import c

pyautogui.PAUSE = 0.8

project_folder = os.getcwd()

# CrtNewDoc()
time.sleep(1)

def Insert_URL_Image():
    if c.click('Insert') is None:
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
    if (pyautogui.locateOnScreen(f'{project_folder}/Pattern/ErrorURL.png', confidence=0.8)) is None:
        pyautogui.press('Escape')  # Escape from active image
        print("something is wrong with clipboard, couldn't paste URL")
    Buttons.right()
    Buttons.enter()  # Next Line

    date = datetime.now().strftime("%d.%m.%Y %H.%M.%S")

    if (pyautogui.locateOnScreen(f'{project_folder}/Pattern/InsertedURLImage.png', confidence=0.9, grayscale=True)) is None:
        pyautogui.screenshot(f'{project_folder}/Completed Tests/Failed/Image/URL/{date}.png')
        f = open(f'{project_folder}/Completed Tests/Tests.txt', 'a')
        f.write(f"{date} - There's a problem with inserting image from URL \n")
        print("There's a problem with inserting image from URL")
    else:
        pyautogui.screenshot(f'{project_folder}/Completed Tests/Success/Image/URL/{date}.png')
        f = open(f'{project_folder}/Completed Tests/Tests.txt', 'a')
        f.write(f"{date} - URL Image inserted successfully \n")


if __name__ == "__main__":
    Insert_URL_Image()