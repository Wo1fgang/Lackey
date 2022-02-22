import pyautogui
import time
import os.path
import pyperclip
from NewDocument import CrtNewDoc
from Insert_Tab import InsertTab
import Buttons
from datetime import datetime

date = datetime.now().strftime("%d.%m.%Y %H.%M.%S")

os.startfile("C:\\Program Files\\ONLYOFFICE\\DesktopEditors\\DesktopEditors.exe")

#time.sleep(7)


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

CrtNewDoc()

InsertTab()

chart()
Buttons.down()
enterChart()

chart()
Buttons.down()
Buttons.right()
enterChart()

if (pyautogui.locateOnScreen('Pattern\\Charts\\1Two.png', confidence=0.8, grayscale=True)) is None:
    pyautogui.screenshot(f'Completed Tests\\Failed\\Chart\\{date}.png')
    f = open('Completed Tests\\Tests.txt', 'a')
    f.write(f"{date} - There's a problem with first two charts \n")
    print('There\'s a problem with first two charts')
    # pyautogui.alert('Something\'s wrong')
    # exit()

Buttons.enter()
Buttons.enter()
pyautogui.press('1')
Buttons.enter()

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
    print('There\'s a problem with second two charts')
    # exit()
    # pyautogui.alert('Something\'s wrong')

Buttons.enter()
Buttons.enter()
pyautogui.press('2')
Buttons.enter()

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
    print('There\'s a problem with third two charts')

Buttons.enter()
Buttons.enter()
pyautogui.press('3')
Buttons.enter()

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
    print('There\'s a problem with fourth two charts')

Buttons.enter()
Buttons.enter()
pyautogui.press('4')
Buttons.enter()

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
    print('There\'s a problem with fifth two charts')

Buttons.enter()
Buttons.enter()
pyautogui.press('5')
Buttons.enter()

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
    print('There\'s a problem with sixth two charts')

Buttons.enter()
Buttons.enter()
pyautogui.press('6')
Buttons.enter()

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
    print('There\'s a problem with seventh two charts')

Buttons.enter()
Buttons.enter()
pyautogui.press('7')
Buttons.enter()

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
    print('There\'s a problem with eighth two charts')

Buttons.enter()
Buttons.enter()
pyautogui.press('8')
Buttons.enter()

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

if (pyautogui.locateOnScreen('Pattern\\Charts\\9Two.png', confidence=0.9, grayscale=True)) is None:
    pyautogui.screenshot(f'Completed Tests\\Failed\\Chart\\{date}.png')
    f = open('Completed Tests\\Tests.txt', 'a')
    f.write(f"{date} - There's a problem with ninth two charts \n")
    print('There\'s a problem with ninth two charts')

Buttons.enter()
Buttons.enter()
pyautogui.press('9')
Buttons.enter()

# ______________________

chart()
Buttons.down()
Buttons.down()
Buttons.down()
Buttons.down()
Buttons.right()
enterChart()

chart()
Buttons.down()
Buttons.down()
Buttons.down()
Buttons.down()
Buttons.right()
Buttons.right()
enterChart()

if (pyautogui.locateOnScreen('Pattern\\Charts\\10Two.png', confidence=0.9, grayscale=True)) is None:
    pyautogui.screenshot(f'Completed Tests\\Failed\\Chart\\{date}.png')
    f = open('Completed Tests\\Tests.txt', 'a')
    f.write(f"{date} - There's a problem with 10th two charts \n")
    print('There\'s a problem with 10th two charts')

Buttons.enter()
Buttons.enter()
pyautogui.press('1')
pyautogui.press('0')
Buttons.enter()

# ____________

chart()
Buttons.down()
Buttons.down()
Buttons.down()
Buttons.down()
Buttons.left()
Buttons.left()
Buttons.left()
enterChart()

chart()
Buttons.down()
Buttons.down()
Buttons.down()
Buttons.down()
Buttons.left()
Buttons.left()
enterChart()

if (pyautogui.locateOnScreen('Pattern\\Charts\\11Two.png', confidence=0.9, grayscale=True)) is None:
    pyautogui.screenshot(f'Completed Tests\\Failed\\Chart\\{date}.png')
    f = open('Completed Tests\\Tests.txt', 'a')
    f.write(f"{date} - There's a problem with 11th two charts \n")
    print('There\'s a problem with 11th two charts')

Buttons.enter()
Buttons.enter()
pyautogui.press('1')
pyautogui.press('1')
Buttons.enter()

# ____________

chart()
Buttons.down()
Buttons.down()
Buttons.down()
Buttons.down()
Buttons.left()
enterChart()

chart()
Buttons.down()
Buttons.down()
Buttons.down()
Buttons.down()
Buttons.down()
enterChart()

if (pyautogui.locateOnScreen('Pattern\\Charts\\12Two.png', confidence=0.9, grayscale=True)) is None:
    pyautogui.screenshot(f'Completed Tests\\Failed\\Chart\\{date}.png')
    f = open('Completed Tests\\Tests.txt', 'a')
    f.write(f"{date} - There's a problem with twelfth two charts \n")
    print('There\'s a problem with twelfth two charts')

Buttons.enter()
Buttons.enter()
pyautogui.press('1')
pyautogui.press('2')
Buttons.enter()

# ____________

chart()
Buttons.down()
Buttons.down()
Buttons.down()
Buttons.down()
Buttons.down()
Buttons.right()
enterChart()

chart()
Buttons.down()
Buttons.down()
Buttons.down()
Buttons.down()
Buttons.down()
Buttons.right()
Buttons.right()
enterChart()

if (pyautogui.locateOnScreen('Pattern\\Charts\\13Two.png', confidence=0.9, grayscale=True)) is None:
    pyautogui.screenshot(f'Completed Tests\\Failed\\Chart\\{date}.png')
    f = open('Completed Tests\\Tests.txt', 'a')
    f.write(f"{date} - There's a problem with 13th two charts \n")
    print('There\'s a problem with 13th two charts')

Buttons.enter()
Buttons.enter()
pyautogui.press('1')
pyautogui.press('3')
Buttons.enter()

# _________________________

chart()
Buttons.down()
Buttons.down()
Buttons.down()
Buttons.down()
Buttons.down()
Buttons.down()
Buttons.left()
Buttons.left()
enterChart()

chart()
Buttons.down()
Buttons.down()
Buttons.down()
Buttons.down()
Buttons.down()
Buttons.down()
enterChart()

if (pyautogui.locateOnScreen('Pattern\\Charts\\14Two.png', confidence=0.9, grayscale=True)) is None:
    pyautogui.screenshot(f'Completed Tests\\Failed\\Chart\\{date}.png')
    f = open('Completed Tests\\Tests.txt', 'a')
    f.write(f"{date} - There's a problem with 14th two charts \n")
    print('There\'s a problem with 14th two charts')

Buttons.enter()
Buttons.enter()
pyautogui.press('1')
pyautogui.press('4')
Buttons.enter()

chart()
Buttons.down()
Buttons.down()
Buttons.down()
Buttons.down()
Buttons.down()
Buttons.down()
Buttons.right()
enterChart()

chart()
Buttons.down()
Buttons.down()
Buttons.down()
Buttons.down()
Buttons.down()
Buttons.down()
Buttons.down()
Buttons.right()
Buttons.right()
enterChart()

if (pyautogui.locateOnScreen('Pattern\\Charts\\15Two.png', confidence=0.9, grayscale=True)) is None:
    pyautogui.screenshot(f'Completed Tests\\Failed\\Chart\\{date}.png')
    f = open('Completed Tests\\Tests.txt', 'a')
    f.write(f"{date} - There's a problem with 15th two charts \n")
    print('There\'s a problem with 15th two charts')

Buttons.enter()
Buttons.enter()
pyautogui.press('1')
pyautogui.press('5')
Buttons.enter()

# ___________

chart()
pyautogui.click(pyautogui.locateOnScreen('Pattern\\Charts\\scatter.png', confidence=0.9, grayscale=True))
enterChart()

chart()
Buttons.down()
Buttons.down()
Buttons.down()
Buttons.down()
Buttons.down()
Buttons.down()
Buttons.left()
enterChart()

if (pyautogui.locateOnScreen('Pattern\\Charts\\16Two.png', confidence=0.9, grayscale=True)) is None:
    pyautogui.screenshot(f'Completed Tests\\Failed\\Chart\\{date}.png')
    f = open('Completed Tests\\Tests.txt', 'a')
    f.write(f"{date} - There's a problem with 15th two charts \n")
    print('There\'s a problem with 16th two charts')

Buttons.enter()
Buttons.enter()
pyautogui.press('1')
pyautogui.press('6')
Buttons.enter()

# __________

chart()
Buttons.up()
Buttons.up()
enterChart()

chart()
Buttons.up()
Buttons.up()
Buttons.right()
enterChart()

if (pyautogui.locateOnScreen('Pattern\\Charts\\17Two.png', confidence=0.9, grayscale=True)) is None:
    pyautogui.screenshot(f'Completed Tests\\Failed\\Chart\\{date}.png')
    f = open('Completed Tests\\Tests.txt', 'a')
    f.write(f"{date} - There's a problem with 17th two charts \n")
    print('There\'s a problem with 17th two charts')

Buttons.enter()
Buttons.enter()
pyautogui.press('1')
pyautogui.press('7')
Buttons.enter()

# _________________

chart()
Buttons.up()
Buttons.up()
Buttons.right()
Buttons.right()
enterChart()

chart()
Buttons.up()
Buttons.up()
Buttons.right()
Buttons.right()
Buttons.right()
enterChart()

if (pyautogui.locateOnScreen('Pattern\\Charts\\18Two.png', confidence=0.9, grayscale=True)) is None:
    pyautogui.screenshot(f'Completed Tests\\Failed\\Chart\\{date}.png')
    f = open('Completed Tests\\Tests.txt', 'a')
    f.write(f"{date} - There's a problem with 18th two charts \n")
    print('There\'s a problem with 18th two charts')

Buttons.enter()
Buttons.enter()
pyautogui.press('1')
pyautogui.press('8')
Buttons.enter()