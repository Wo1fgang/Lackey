import pyautogui
import time
import os.path
import pyperclip  # Library for copypasting stuff
from datetime import datetime
import Buttons

pyautogui.PAUSE = 0.7

time.sleep(2)

project_folder = os.getcwd()


def Insert_Local_Image():
    # Local - Insert tab + Insert Local Image
    def local():
        # INSERTING LOCAL IMAGE
        pyautogui.press('alt')
        pyautogui.press('i')
        pyautogui.press('e')
        Buttons.down()  # Choosing insert local image
        Buttons.enter()  # OK
        time.sleep(1)

    # Inserting image name
    def ii():
        pyautogui.hotkey('Ctrl', 'v')
        Buttons.enter()
        Buttons.escape()  # Escape from active image
        Buttons.right()
        # pyautogui.press('Enter')  # Next Line

    local()
    pyperclip.copy('C:\Lackey\Images\small images\JPG.jpg')
    ii()

    local()
    pyperclip.copy('C:\Lackey\Images\small images\BMP.bmp')
    ii()

    local()
    #pyautogui.click(pyautogui.locateOnScreen('Pattern\\FileName.png', confidence=0.9, grayscale=True))
    pyperclip.copy('C:\Lackey\Images\small images\PNG.png')
    ii()

    local()
    #pyautogui.click(pyautogui.locateOnScreen('Pattern\\FileName.png', confidence=0.9, grayscale=True))
    pyperclip.copy('C:\Lackey\Images\small images\TIFF.tiff')
    ii()

    local()
    #pyautogui.click(pyautogui.locateOnScreen('Pattern\\FileName.png', confidence=0.9, grayscale=True))
    pyperclip.copy('C:\Lackey\Images\small images\GIF.gif')
    ii()

    date = datetime.now().strftime("%d.%m.%Y %H.%M.%S")

    if (pyautogui.locateOnScreen(f'{project_folder}/Images/small images/Correct.png', confidence=0.9,
                                 grayscale=True)) is None:  # If not image in opened explorer menu
        pyautogui.screenshot(f'{project_folder}/Completed Tests/Failed/Image/Local/{date}.png')
        f = open(f'{project_folder}/Completed Tests/Tests.txt', 'a')
        f.write(f"{date} - There's a problem with inserting local image \n")
    else:
        pyautogui.screenshot(f'{project_folder}/Completed Tests/Success/Image/Local/{date}.png')
        f = open(f'{project_folder}/Completed Tests/Tests.txt', 'a')
        f.write(f"{date} - Local Image inserted successfully \n")


if __name__ == "__main__":
    Insert_Local_Image()
