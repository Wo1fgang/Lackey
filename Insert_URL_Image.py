import pyautogui
import os.path
import pyperclip
from Insert_Tab import InsertTab
from NewDocument import CrtNewDoc
from datetime import datetime
import Buttons

pyautogui.PAUSE = 0.5

os.chdir('C:\\Auto')


# CrtNewDoc()


def Insert_URL_Image():
    InsertTab()
    # INSERTING IMAGE FROM URL:
    pyautogui.click(pyautogui.locateOnScreen('Image.png', confidence=0.9, grayscale=True))
    Buttons.down()
    Buttons.down()  # Choosing insert from URL
    Buttons.enter()  # OK
    pyperclip.copy('https://pbs.twimg.com/media/FI46f4eXwAMcKW-?format=jpg&name=medium')
    pyautogui.hotkey('Ctrl', 'v')  # Insert Image URL
    Buttons.enter()
    if (pyautogui.locateOnScreen('ErrorURL.png', confidence=0.8)) is None:
        pyautogui.press('Escape')  # Escape from active image
    else:
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('alt', 'shift')
        pyautogui.typewrite('https://pbs.twimg.com/media/FI46f4eXwAMcKW-?format=jpg&name=medium')
    Buttons.right()
    Buttons.enter()  # Next Line

    date = datetime.now().strftime("%d.%m.%Y %H.%M.%S")

    if (pyautogui.locateOnScreen('InsertedURLImage.png', confidence=0.9, grayscale=True)) is None:
        pyautogui.screenshot(f'C:\\Auto\\Completed Tests\\Failed\\Image\\URL\\{date}.png')
        f = open('C:\\Auto\\Completed Tests\\Tests.txt', 'a')
        f.write(f"{date} - There's a problem with inserting image from URL \n")
    else:
        pyautogui.screenshot(f'C:\\Auto\\Completed Tests\\Success\\Image\\URL\\{date}.png')
        f = open('C:\\Auto\\Completed Tests\\Tests.txt', 'a')
        f.write(f"{date} - URL Image inserted successfully \n")

# If we want to just use this test, uncomment next line

# Insert_URL_Image()