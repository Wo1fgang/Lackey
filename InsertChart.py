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


def down():
    pyautogui.press('Down')


pyautogui.PAUSE = 0.5


def next():
    Buttons.escape()
    Buttons.right()
    Buttons.enter()

os.startfile("C:\\Program Files\\ONLYOFFICE\\DesktopEditors\\DesktopEditors.exe")

CrtNewDoc()

InsertTab()

pyautogui.click(pyautogui.locateOnScreen('Pattern\\Chart.png', confidence=0.9, grayscale=True))
Buttons.down()
Buttons.enter()
time.sleep(5)
pyautogui.click(pyautogui.locateOnScreen('Pattern\\SaveAndExit.png', confidence=0.9, grayscale=True))
time.sleep(1)
next()

pyautogui.click(pyautogui.locateOnScreen('Pattern\\Chart.png', confidence=0.9, grayscale=True))
Buttons.down()
Buttons.right()
Buttons.enter()
time.sleep(4)
pyautogui.click(pyautogui.locateOnScreen('Pattern\\SaveAndExit.png', confidence=0.9, grayscale=True))
time.sleep(1)
next()

if (pyautogui.locateOnScreen('Pattern\\Charts\\FirstTwo.png', confidence=0.9, grayscale=True)) is None:
    pyautogui.screenshot(f'Completed Tests\\Failed\\Chart\\{date}.png')
    f = open('Completed Tests\\Tests.txt', 'a')
    f.write(f"{date} - There's a problem with first two charts \n")
    # pyautogui.alert('Something\'s wrong')
    # exit()

pyautogui.click(pyautogui.locateOnScreen('Pattern\\Chart.png', confidence=0.9, grayscale=True))
Buttons.down()
Buttons.right()
Buttons.right()
Buttons.enter()
time.sleep(4)
pyautogui.click(pyautogui.locateOnScreen('Pattern\\SaveAndExit.png', confidence=0.9, grayscale=True))
time.sleep(1)
next()

pyautogui.click(pyautogui.locateOnScreen('Pattern\\Chart.png', confidence=0.9, grayscale=True))
Buttons.down()
Buttons.right()
Buttons.right()
Buttons.right()
Buttons.enter()
time.sleep(4)
pyautogui.click(pyautogui.locateOnScreen('Pattern\\SaveAndExit.png', confidence=0.9, grayscale=True))
time.sleep(1)
next()

if (pyautogui.locateOnScreen('Pattern\\Charts\\SecondTwo.png', confidence=0.9, grayscale=True)) is None:
    pyautogui.screenshot(f'Completed Tests\\Failed\\Chart\\{date}.png')
    f = open('Completed Tests\\Tests.txt', 'a')
    f.write(f"{date} - There's a problem with first two charts \n")
    # exit()
    # pyautogui.alert('Something\'s wrong')

pyautogui.click(pyautogui.locateOnScreen('Pattern\\Chart.png', confidence=0.9, grayscale=True))
Buttons.down()
Buttons.right()
Buttons.right()
Buttons.right()
Buttons.right()
Buttons.enter()
time.sleep(4)
pyautogui.click(pyautogui.locateOnScreen('Pattern\\SaveAndExit.png', confidence=0.9, grayscale=True))
time.sleep(1)
next()

pyautogui.click(pyautogui.locateOnScreen('Pattern\\Chart.png', confidence=0.9, grayscale=True))
Buttons.down()
Buttons.left()
Buttons.left()
Buttons.enter()
time.sleep(4)
pyautogui.click(pyautogui.locateOnScreen('Pattern\\SaveAndExit.png', confidence=0.9, grayscale=True))
time.sleep(1)
next()

if (pyautogui.locateOnScreen('Pattern\\Charts\\ThirdTwo.png', confidence=0.9, grayscale=True)) is None:
    pyautogui.screenshot(f'Completed Tests\\Failed\\Chart\\{date}.png')
    f = open('Completed Tests\\Tests.txt', 'a')
    f.write(f"{date} - There's a problem with first two charts \n")

pyautogui.click(pyautogui.locateOnScreen('Pattern\\Chart.png', confidence=0.9, grayscale=True))
Buttons.down()
Buttons.left()
Buttons.enter()
time.sleep(4)
pyautogui.click(pyautogui.locateOnScreen('Pattern\\SaveAndExit.png', confidence=0.9, grayscale=True))
time.sleep(1)
next()

pyautogui.click(pyautogui.locateOnScreen('Pattern\\Chart.png', confidence=0.9, grayscale=True))
Buttons.down()
Buttons.down()
Buttons.enter()
time.sleep(4)
pyautogui.click(pyautogui.locateOnScreen('Pattern\\SaveAndExit.png', confidence=0.9, grayscale=True))
time.sleep(1)
next()

if (pyautogui.locateOnScreen('Pattern\\Charts\\FourthTwo.png', confidence=0.9, grayscale=True)) is None:
    pyautogui.screenshot(f'Completed Tests\\Failed\\Chart\\{date}.png')
    f = open('Completed Tests\\Tests.txt', 'a')
    f.write(f"{date} - There's a problem with first two charts \n")

pyautogui.click(pyautogui.locateOnScreen('Pattern\\Chart.png', confidence=0.9, grayscale=True))
Buttons.down()
Buttons.down()
Buttons.right()
Buttons.enter()
time.sleep(4)
pyautogui.click(pyautogui.locateOnScreen('Pattern\\SaveAndExit.png', confidence=0.9, grayscale=True))
time.sleep(1)
next()

pyautogui.click(pyautogui.locateOnScreen('Pattern\\Chart.png', confidence=0.9, grayscale=True))
Buttons.down()
Buttons.down()
Buttons.right()
Buttons.right()
Buttons.enter()
time.sleep(4)
pyautogui.click(pyautogui.locateOnScreen('Pattern\\SaveAndExit.png', confidence=0.9, grayscale=True))
time.sleep(1)
next()

if (pyautogui.locateOnScreen('Pattern\\Charts\\5Two.png', confidence=0.9, grayscale=True)) is None:
    pyautogui.screenshot(f'Completed Tests\\Failed\\Chart\\{date}.png')
    f = open('Completed Tests\\Tests.txt', 'a')
    f.write(f"{date} - There's a problem with first two charts \n")

pyautogui.click(pyautogui.locateOnScreen('Pattern\\Chart.png', confidence=0.9, grayscale=True))
Buttons.down()
Buttons.down()
Buttons.right()
Buttons.right()
Buttons.right()
Buttons.enter()
time.sleep(4)
pyautogui.click(pyautogui.locateOnScreen('Pattern\\SaveAndExit.png', confidence=0.9, grayscale=True))
time.sleep(1)
next()

pyautogui.click(pyautogui.locateOnScreen('Pattern\\Chart.png', confidence=0.9, grayscale=True))
Buttons.down()
Buttons.down()
Buttons.right()
Buttons.right()
Buttons.right()
Buttons.right()
Buttons.enter()
time.sleep(4)
pyautogui.click(pyautogui.locateOnScreen('Pattern\\SaveAndExit.png', confidence=0.9, grayscale=True))
time.sleep(1)
next()

if (pyautogui.locateOnScreen('Pattern\\Charts\\6Two.png', confidence=0.9, grayscale=True)) is None:
    pyautogui.screenshot(f'Completed Tests\\Failed\\Chart\\{date}.png')
    f = open('Completed Tests\\Tests.txt', 'a')
    f.write(f"{date} - There's a problem with first two charts \n")

pyautogui.click(pyautogui.locateOnScreen('Pattern\\Chart.png', confidence=0.9, grayscale=True))
Buttons.down()
Buttons.down()
Buttons.left()
Buttons.left()
Buttons.enter()
time.sleep(4)
pyautogui.click(pyautogui.locateOnScreen('Pattern\\SaveAndExit.png', confidence=0.9, grayscale=True))
time.sleep(1)
next()

pyautogui.click(pyautogui.locateOnScreen('Pattern\\Chart.png', confidence=0.9, grayscale=True))
Buttons.down()
Buttons.down()
Buttons.left()
Buttons.enter()
time.sleep(4)
pyautogui.click(pyautogui.locateOnScreen('Pattern\\SaveAndExit.png', confidence=0.9, grayscale=True))
time.sleep(1)
next()

if (pyautogui.locateOnScreen('Pattern\\Charts\\7Two.png', confidence=0.9, grayscale=True)) is None:
    pyautogui.screenshot(f'Completed Tests\\Failed\\Chart\\{date}.png')
    f = open('Completed Tests\\Tests.txt', 'a')
    f.write(f"{date} - There's a problem with first two charts \n")