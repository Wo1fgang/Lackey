import pyautogui
import time
import os.path
import pyperclip  # Library for copypasting stuff
from datetime import datetime
import Buttons
import GoFullscreen
import c
import csv
import NewDocument

GoFullscreen.goFullScreen()

pyautogui.PAUSE = 0.7

time.sleep(2)

project_folder = os.getcwd()

test = os.path.basename(__file__)

LocalImage = ["JPG.jpg",
              "BMP.bmp",
              "PNG.png",
              "TIFF.tiff",
              "GIF.gif"]


def Insert_Local_Image():
    # Local - Insert tab + Insert Local Image
    NewDocument.CrtNewDoc()

    def local():
        # INSERTING LOCAL IMAGE
        if pyautogui.click(pyautogui.locateOnScreen(f'{project_folder}/Pattern/Insert.png', confidence=0.9)) is None:
            c.click('Insert2')
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

    def CheckLocal(LI):
        local()
        if os.name == "nt":
            pyperclip.copy(f'{project_folder}\Pattern\Images\small images\{LI}')
        else:
            pyperclip.copy(f'{project_folder}/Pattern/Images/small images/{LI}')
        ii()

    for LI in LocalImage:
        CheckLocal(LI)

    date = datetime.now().strftime("%d.%m.%Y %H.%M.%S")

    if (pyautogui.locateOnScreen(f'{project_folder}/Pattern/Images/small images/Correct.png',
                                 confidence=0.9, grayscale=True)) is None:
        pyautogui.screenshot(f'{project_folder}/Completed Tests/Failed/Image/Local/{date}.png')
        with open('Completed Tests.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=' ')
            writer.writerow([f"{date}', {test}, FAILED"])
        print("There's a problem with inserting local image")
    else:
        with open('Completed Tests.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=' ')
            writer.writerow([f"{date}, {test}, SUCCESS"])

    pyautogui.hotkey('Ctrl', 'w')
    Buttons.tab()
    Buttons.enter()


if __name__ == "__main__":
    Insert_Local_Image()
