import pyautogui
import os
import Buttons
import pyperclip
import time
from datetime import datetime
import NewDocument

os.startfile("C:\\Program Files\\ONLYOFFICE\\DesktopEditors\\DesktopEditors.exe") # Launching DesktopEditor
time.sleep(8)

pyautogui.PAUSE = 0.5

date = datetime.now().strftime("%d.%m.%Y %H.%M.%S")  # date = Current date in "d.m.Y H.M.S" format

# Changing username
pyautogui.click(pyautogui.locateOnScreen('Pattern\\Settings.png', confidence=0.9, grayscale=True))
Buttons.tab()
pyperclip.copy('Some text to check if changing username works')
pyautogui.hotkey('Ctrl', 'v')
pyautogui.click(pyautogui.locateOnScreen('Pattern\\Apply.png', confidence=0.9, grayscale=True))

if (pyautogui.locateOnScreen('Pattern\\ChangedUsername.png', confidence=0.9,
                             grayscale=True)) is None:
    f = open('Completed Tests\\Tests.txt', 'a')  # Open Tests.txt
    f.write(f"{date} - There's a problem with changing username \n")  # Write down that something's wrong
else:
    f = open('Completed Tests\\Tests.txt', 'a')
    f.write(f"{date} - Username changed successfully \n")  # Same if everything is alright

pyautogui.click(pyautogui.locateOnScreen('Pattern\\ResetToDefault.png', confidence=0.9, grayscale=True))
pyautogui.click(pyautogui.locateOnScreen('Pattern\\Apply.png', confidence=0.9, grayscale=True))


# Changing interface scaling

def ChangeInterfaceScaling():
    pyautogui.click(pyautogui.locateOnScreen('Pattern\\Settings.png', confidence=0.9, grayscale=True))
    Buttons.tab()
    Buttons.tab()
    Buttons.tab()
    Buttons.tab()
    Buttons.down()
    Buttons.enter()
    pyautogui.click(pyautogui.locateOnScreen('Pattern\\Apply.png', confidence=0.9, grayscale=True))


# Cheking 100%
ChangeInterfaceScaling()
NewDocument.CrtNewDoc()
if (pyautogui.locateOnScreen('Pattern\\InterfaceScaling\\100\\Document.png', confidence=0.9,
                             grayscale=True)) is None:
    f = open('Completed Tests\\Tests.txt', 'a')  # Open Tests.txt
    f.write(
        f"{date} - There's a problem with document at 100% interface scaling \n")  # Write down that something's wrong
else:
    f = open('Completed Tests\\Tests.txt', 'a')
    f.write(f"{date} - Everything's alright with document at 100% interface scaling \n")  # Same if everything is alright

NewDocument.CrtNewSpreadsheet()
if (pyautogui.locateOnScreen('Pattern\\InterfaceScaling\\100\\Spreadsheet.png', confidence=0.9,
                             grayscale=True)) is None:
    f = open('Completed Tests\\Tests.txt', 'a')  # Open Tests.txt
    f.write(
        f"{date} - There's a problem with Spreadsheet at 100% interface scaling \n")  # Write down that something's wrong
else:
    f = open('Completed Tests\\Tests.txt', 'a')
    f.write(
        f"{date} - Everything's alright with Spreadsheet at 100% interface scaling \n")  # Same if everything is alright

NewDocument.CrtNewPresentation()
if (pyautogui.locateOnScreen('Pattern\\InterfaceScaling\\100\\Presentation.png', confidence=0.9,
                             grayscale=True)) is None:
    f = open('Completed Tests\\Tests.txt', 'a')  # Open Tests.txt
    f.write(
        f"{date} - There's a problem with Presentation at 100% interface scaling \n")  # Write down that something's wrong
else:
    f = open('Completed Tests\\Tests.txt', 'a')
    f.write(
        f"{date} - Everything's alright with Presentation at 100% interface scaling \n")  # Same if everything is alright

pyautogui.click(pyautogui.locateOnScreen('Pattern\\MainMenu.png', confidence=0.9, grayscale=True))

# Cheking 125%
ChangeInterfaceScaling()
NewDocument.CrtNewDoc()
if (pyautogui.locateOnScreen('Pattern\\InterfaceScaling\\125\\Document.png', confidence=0.9,
                             grayscale=True)) is None:
    f = open('Completed Tests\\Tests.txt', 'a')  # Open Tests.txt
    f.write(
        f"{date} - There's a problem with document at 125% interface scaling \n")  # Write down that something's wrong
else:
    f = open('Completed Tests\\Tests.txt', 'a')
    f.write(f"{date} - Everything's alright with document at 125% interface scaling \n")  # Same if everything is alright
pyautogui.click(pyautogui.locateOnScreen('Pattern\\MainMenu125.png', confidence=0.9, grayscale=True))

NewDocument.CrtNewSpreadsheet()
if (pyautogui.locateOnScreen('Pattern\\InterfaceScaling\\125\\Spreadsheet.png', confidence=0.9,
                             grayscale=True)) is None:
    f = open('Completed Tests\\Tests.txt', 'a')  # Open Tests.txt
    f.write(
        f"{date} - There's a problem with Spreadsheet at 125% interface scaling \n")  # Write down that something's wrong
else:
    f = open('Completed Tests\\Tests.txt', 'a')
    f.write(
        f"{date} - Everything's alright with Spreadsheet at 125% interface scaling \n")  # Same if everything is alright
pyautogui.click(pyautogui.locateOnScreen('Pattern\\MainMenu125.png', confidence=0.9, grayscale=True))

NewDocument.CrtNewPresentation()
if (pyautogui.locateOnScreen('Pattern\\InterfaceScaling\\125\\Presentation.png', confidence=0.9,
                             grayscale=True)) is None:
    f = open('Completed Tests\\Tests.txt', 'a')  # Open Tests.txt
    f.write(
        f"{date} - There's a problem with Presentation at 125% interface scaling \n")  # Write down that something's wrong
else:
    f = open('Completed Tests\\Tests.txt', 'a')
    f.write(
        f"{date} - Everything's alright with Presentation at 125% interface scaling \n")  # Same if everything is alright

pyautogui.click(pyautogui.locateOnScreen('Pattern\\MainMenu125.png', confidence=0.9, grayscale=True))

# Cheking 150%
ChangeInterfaceScaling()
NewDocument.CrtNewDoc()
if (pyautogui.locateOnScreen('Pattern\\InterfaceScaling\\150\\Document.png', confidence=0.9,
                             grayscale=True)) is None:
    f = open('Completed Tests\\Tests.txt', 'a')  # Open Tests.txt
    f.write(
        f"{date} - There's a problem with document at 150% interface scaling \n")  # Write down that something's wrong
else:
    f = open('Completed Tests\\Tests.txt', 'a')
    f.write(f"{date} - Everything's alright with document at 150% interface scaling \n")  # Same if everything is alright
pyautogui.click(pyautogui.locateOnScreen('Pattern\\MainMenu150.png', confidence=0.9, grayscale=True))

NewDocument.CrtNewSpreadsheet()
if (pyautogui.locateOnScreen('Pattern\\InterfaceScaling\\150\\Spreadsheet.png', confidence=0.9,
                             grayscale=True)) is None:
    f = open('Completed Tests\\Tests.txt', 'a')  # Open Tests.txt
    f.write(
        f"{date} - There's a problem with Spreadsheet at 150% interface scaling \n")  # Write down that something's wrong
else:
    f = open('Completed Tests\\Tests.txt', 'a')
    f.write(
        f"{date} - Everything's alright with Spreadsheet at 150% interface scaling \n")  # Same if everything is alright
pyautogui.click(pyautogui.locateOnScreen('Pattern\\MainMenu150.png', confidence=0.9, grayscale=True))

NewDocument.CrtNewPresentation()
if (pyautogui.locateOnScreen('Pattern\\InterfaceScaling\\150\\Presentation.png', confidence=0.9,
                             grayscale=True)) is None:
    f = open('Completed Tests\\Tests.txt', 'a')  # Open Tests.txt
    f.write(
        f"{date} - There's a problem with Presentation at 150% interface scaling \n")  # Write down that something's wrong
else:
    f = open('Completed Tests\\Tests.txt', 'a')
    f.write(
        f"{date} - Everything's alright with Presentation at 150% interface scaling \n")  # Same if everything is alright

pyautogui.click(pyautogui.locateOnScreen('Pattern\\MainMenu150.png', confidence=0.9, grayscale=True))

# Cheking 175%
ChangeInterfaceScaling()
NewDocument.CrtNewDoc()
if (pyautogui.locateOnScreen('Pattern\\InterfaceScaling\\175\\Document.png', confidence=0.9,
                             grayscale=True)) is None:
    f = open('Completed Tests\\Tests.txt', 'a')  # Open Tests.txt
    f.write(
        f"{date} - There's a problem with document at 175% interface scaling \n")  # Write down that something's wrong
else:
    f = open('Completed Tests\\Tests.txt', 'a')
    f.write(f"{date} - Everything's alright with document at 175% interface scaling \n")  # Same if everything is alright
pyautogui.click(pyautogui.locateOnScreen('Pattern\\MainMenu175.png', confidence=0.9, grayscale=True))

NewDocument.CrtNewSpreadsheet()
if (pyautogui.locateOnScreen('Pattern\\InterfaceScaling\\175\\Spreadsheet.png', confidence=0.9,
                             grayscale=True)) is None:
    f = open('Completed Tests\\Tests.txt', 'a')  # Open Tests.txt
    f.write(
        f"{date} - There's a problem with Spreadsheet at 175% interface scaling \n")  # Write down that something's wrong
else:
    f = open('Completed Tests\\Tests.txt', 'a')
    f.write(
        f"{date} - Everything's alright with Spreadsheet at 175% interface scaling \n")  # Same if everything is alright
pyautogui.click(pyautogui.locateOnScreen('Pattern\\MainMenu175.png', confidence=0.9, grayscale=True))

NewDocument.CrtNewPresentation()
if (pyautogui.locateOnScreen('Pattern\\InterfaceScaling\\175\\Presentation.png', confidence=0.9,
                             grayscale=True)) is None:
    f = open('Completed Tests\\Tests.txt', 'a')  # Open Tests.txt
    f.write(
        f"{date} - There's a problem with Presentation at 175% interface scaling \n")  # Write down that something's wrong
else:
    f = open('Completed Tests\\Tests.txt', 'a')
    f.write(
        f"{date} - Everything's alright with Presentation at 175% interface scaling \n")  # Same if everything is alright

pyautogui.click(pyautogui.locateOnScreen('Pattern\\MainMenu175.png', confidence=0.9, grayscale=True))

# Cheking 200%
ChangeInterfaceScaling()
NewDocument.CrtNewDoc()
if (pyautogui.locateOnScreen('Pattern\\InterfaceScaling\\200\\Document.png', confidence=0.9,
                             grayscale=True)) is None:
    f = open('Completed Tests\\Tests.txt', 'a')  # Open Tests.txt
    f.write(
        f"{date} - There's a problem with document at 200% interface scaling \n")  # Write down that something's wrong
else:
    f = open('Completed Tests\\Tests.txt', 'a')
    f.write(f"{date} - Everything's alright with document at 200% interface scaling \n")  # Same if everything is alright
pyautogui.click(pyautogui.locateOnScreen('Pattern\\MainMenu200.png', confidence=0.9, grayscale=True))

NewDocument.CrtNewSpreadsheet()
if (pyautogui.locateOnScreen('Pattern\\InterfaceScaling\\200\\Spreadsheet.png', confidence=0.9,
                             grayscale=True)) is None:
    f = open('Completed Tests\\Tests.txt', 'a')  # Open Tests.txt
    f.write(
        f"{date} - There's a problem with Spreadsheet at 200% interface scaling \n")  # Write down that something's wrong
else:
    f = open('Completed Tests\\Tests.txt', 'a')
    f.write(
        f"{date} - Everything's alright with Spreadsheet at 200% interface scaling \n")  # Same if everything is alright
pyautogui.click(pyautogui.locateOnScreen('Pattern\\MainMenu200.png', confidence=0.9, grayscale=True))

NewDocument.CrtNewPresentation()
if (pyautogui.locateOnScreen('Pattern\\InterfaceScaling\\200\\Presentation.png', confidence=0.9,
                             grayscale=True)) is None:
    f = open('Completed Tests\\Tests.txt', 'a')  # Open Tests.txt
    f.write(
        f"{date} - There's a problem with Presentation at 200% interface scaling \n")  # Write down that something's wrong
else:
    f = open('Completed Tests\\Tests.txt', 'a')
    f.write(
        f"{date} - Everything's alright with Presentation at 200% interface scaling \n")  # Same if everything is alright

pyautogui.click(pyautogui.locateOnScreen('Pattern\\MainMenu200.png', confidence=0.9, grayscale=True))

ChangeInterfaceScaling()
