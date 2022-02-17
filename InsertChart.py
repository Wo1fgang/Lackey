import pyautogui
import time
import os.path
import pyperclip
from datetime import datetime
from NewDocument import CrtNewDoc
from Insert_Tab import InsertTab
import Buttons
from datetime import datetime

date = datetime.now().strftime("%d.%m.%Y %H.%M.%S")

# os.startfile("C:\\Program Files\\ONLYOFFICE\\DesktopEditors\\DesktopEditors.exe")
#
# time.sleep(7)

def next():
    Buttons.escape()
    Buttons.right()


def enterChart():
    Buttons.enter()
    time.sleep(5)
    pyautogui.click(pyautogui.locateOnScreen('Pattern\\SaveAndExit.png', confidence=0.9, grayscale=True))
    time.sleep(1)
    next()


def chart():
    pyautogui.click(pyautogui.locateOnScreen('Pattern\\Chart.png', confidence=0.9, grayscale=True))

pyautogui.PAUSE = 0.5

os.startfile("C:\\Program Files\\ONLYOFFICE\\DesktopEditors\\DesktopEditors.exe")

CrtNewDoc()

InsertTab()

chart()
Buttons.down()
enterChart()


chart()
Buttons.down()
Buttons.right()
enterChart()

if (pyautogui.locateOnScreen('Pattern\\Charts\\1Two.png', confidence=0.9, grayscale=True)) is None:
    pyautogui.screenshot(f'Completed Tests\\Failed\\Chart\\{date}.png')
    f = open('Completed Tests\\Tests.txt', 'a')
    f.write(f"{date} - There's a problem with first two charts \n")
    # pyautogui.alert('Something\'s wrong')
    # exit()

Buttons.enter()
Buttons.enter()
pyautogui.press('First two')

chart()
Buttons.down()
Buttons.right()
Buttons.right()
enterChart()

chart()
Buttons.down()
Buttons.right()
Buttons.right()
Buttons.right()
enterChart()

if (pyautogui.locateOnScreen('Pattern\\Charts\\2Two.png', confidence=0.9, grayscale=True)) is None:
    pyautogui.screenshot(f'Completed Tests\\Failed\\Chart\\{date}.png')
    f = open('Completed Tests\\Tests.txt', 'a')
    f.write(f"{date} - There's a problem with second two charts \n")
    # exit()
    # pyautogui.alert('Something\'s wrong')

Buttons.enter()
Buttons.enter()
pyautogui.press('Second two')

chart()
Buttons.down()
Buttons.right()
Buttons.right()
Buttons.right()
Buttons.right()
enterChart()

chart()
Buttons.down()
Buttons.left()
Buttons.left()
enterChart()

if (pyautogui.locateOnScreen('Pattern\\Charts\\3Two.png', confidence=0.9, grayscale=True)) is None:
    pyautogui.screenshot(f'Completed Tests\\Failed\\Chart\\{date}.png')
    f = open('Completed Tests\\Tests.txt', 'a')
    f.write(f"{date} - There's a problem with third two charts \n")

Buttons.enter()
Buttons.enter()
pyautogui.press('Third two')

chart()
Buttons.down()
Buttons.left()
enterChart()

chart()
Buttons.down()
Buttons.down()
enterChart()

if (pyautogui.locateOnScreen('Pattern\\Charts\\4Two.png', confidence=0.9, grayscale=True)) is None:
    pyautogui.screenshot(f'Completed Tests\\Failed\\Chart\\{date}.png')
    f = open('Completed Tests\\Tests.txt', 'a')
    f.write(f"{date} - There's a problem with fourth two charts \n")

Buttons.enter()
Buttons.enter()
pyautogui.press('Fourth two')

chart()
Buttons.down()
Buttons.down()
Buttons.right()
enterChart()

chart()
Buttons.down()
Buttons.down()
Buttons.right()
Buttons.right()
enterChart()

if (pyautogui.locateOnScreen('Pattern\\Charts\\5Two.png', confidence=0.9, grayscale=True)) is None:
    pyautogui.screenshot(f'Completed Tests\\Failed\\Chart\\{date}.png')
    f = open('Completed Tests\\Tests.txt', 'a')
    f.write(f"{date} - There's a problem with fifth two charts \n")

Buttons.enter()
Buttons.enter()
pyautogui.press('Fifth two')

chart()
Buttons.down()
Buttons.down()
Buttons.right()
Buttons.right()
Buttons.right()
enterChart()

chart()
Buttons.down()
Buttons.down()
Buttons.right()
Buttons.right()
Buttons.right()
Buttons.right()
enterChart()

if (pyautogui.locateOnScreen('Pattern\\Charts\\6Two.png', confidence=0.9, grayscale=True)) is None:
    pyautogui.screenshot(f'Completed Tests\\Failed\\Chart\\{date}.png')
    f = open('Completed Tests\\Tests.txt', 'a')
    f.write(f"{date} - There's a problem with sixth two charts \n")

Buttons.enter()
Buttons.enter()
pyautogui.press('Sixth two')

chart()
Buttons.down()
Buttons.down()
Buttons.left()
Buttons.left()
enterChart()

chart()
Buttons.down()
Buttons.down()
Buttons.left()
enterChart()

if (pyautogui.locateOnScreen('Pattern\\Charts\\7Two.png', confidence=0.9, grayscale=True)) is None:
    pyautogui.screenshot(f'Completed Tests\\Failed\\Chart\\{date}.png')
    f = open('Completed Tests\\Tests.txt', 'a')
    f.write(f"{date} - There's a problem with seventh two charts \n")

Buttons.enter()
Buttons.enter()
pyautogui.press('Seventh two')

chart()
Buttons.down()
Buttons.down()
Buttons.down()
enterChart()

chart()
Buttons.down()
Buttons.down()
Buttons.down()
Buttons.right()
enterChart()

if (pyautogui.locateOnScreen('Pattern\\Charts\\8Two.png', confidence=0.9, grayscale=True)) is None:
    pyautogui.screenshot(f'Completed Tests\\Failed\\Chart\\{date}.png')
    f = open('Completed Tests\\Tests.txt', 'a')
    f.write(f"{date} - There's a problem with eighth two charts \n")

Buttons.enter()
Buttons.enter()
pyautogui.press('Eighth two')

chart()
Buttons.down()
Buttons.down()
Buttons.down()
Buttons.right()
Buttons.right()
enterChart()

chart()
Buttons.down()
Buttons.down()
Buttons.down()
Buttons.down()
enterChart()