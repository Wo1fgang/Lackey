import pyautogui
import time
import os.path
import pyperclip
from datetime import datetime
from Insert_Tab import InsertTab
import Buttons

pyautogui.PAUSE = 0.5

os.chdir('C:\\Auto')


def Insert_Local_Image():
    InsertTab()

    # Local - Insert tab + Insert Local Image
    def local():
        pyautogui.click(pyautogui.locateOnScreen('Insert.png', confidence=0.9, grayscale=True))  # Click on Insert
        time.sleep(0.5)

        # INSERTING LOCAL IMAGE
        pyautogui.click(pyautogui.locateOnScreen('Image.png', confidence=0.9, grayscale=True))
        Buttons.down()  # Choosing insert local image
        Buttons.enter()  # OK
        time.sleep(1)

    # Inserting imagename
    def ii():
        pyautogui.hotkey('Ctrl', 'v')
        Buttons.enter()
        pyautogui.press('Escape')  # Escape from active image
        Buttons.right()
        # pyautogui.press('Enter')  # Next Line

    local()
    # Change directory in explorer
    pyautogui.click(pyautogui.locateOnScreen('QuickAccess.png', confidence=0.9, grayscale=True))
    pyautogui.click(pyautogui.locateOnScreen('AddressBar.png', confidence=0.9, grayscale=True))
    pyperclip.copy('C:\Auto\Images\small images')
    pyautogui.hotkey('Ctrl', 'v')
    Buttons.enter()

    pyautogui.click(pyautogui.locateOnScreen('FileName.png', confidence=0.9, grayscale=True))
    pyperclip.copy('jpg.jpg')
    ii()

    local()
    pyautogui.click(pyautogui.locateOnScreen('FileName.png', confidence=0.9, grayscale=True))
    pyperclip.copy('png.png')
    ii()

    local()
    pyautogui.click(pyautogui.locateOnScreen('FileName.png', confidence=0.9, grayscale=True))
    pyperclip.copy('tiff.tiff')
    ii()

    local()
    pyautogui.click(pyautogui.locateOnScreen('FileName.png', confidence=0.9, grayscale=True))
    pyperclip.copy('bmp.bmp')
    ii()

    local()
    pyautogui.click(pyautogui.locateOnScreen('FileName.png', confidence=0.9, grayscale=True))
    pyperclip.copy('gif.gif')
    ii()

    date = datetime.now().strftime("%d.%m.%Y %H.%M.%S")

    if (pyautogui.locateOnScreen('C:\Auto\Images\small images\Correct.png', confidence=0.9,
                                 grayscale=True)) is None:  # If not image in opened explorer menu
        pyautogui.screenshot(f"C:\\Auto\\Completed Tests\\Failed\\Image\\Local\\{date}.png")
        f = open('C:\\Auto\\Completed Tests\\Tests.txt', 'a')
        f.write(f"{date} - There's a problem with inserting local image \n")
    else:
        pyautogui.screenshot(f"C:\\Auto\\Completed Tests\\Success\\Image\\Local\\{date}.png")
        f = open('C:\\Auto\\Completed Tests\\Tests.txt', 'a')
        f.write(f"{date} - Local Image inserted successfully \n")