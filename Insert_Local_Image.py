import pyautogui
import time
import os.path
import pyperclip  # Library for copypasting stuff
from datetime import datetime
import Buttons
import GoFullscreen
import clicker
import csv
import NewDocument
import Change_Theme

Change_Theme.ChangeThemeToLight()

GoFullscreen.goFullScreen()

pyautogui.PAUSE = 0.7

time.sleep(2)

project_folder = os.getcwd()

test = os.path.basename(__file__)

Formats = ["jpg.jpg",
           "bmp.bmp",
           "png.png",
           "tiff.tiff",
           "gif.gif",
           "JPG_.JPG",
           "BMP_.BMP",
           "PNG_.PNG",
           "TIFF_.TIFF",
           "GIF_.GIF"]

date = datetime.now().strftime("%d.%m.%Y %H.%M.%S")

day_of_test = datetime.now().strftime("%d.%m.%Y %H")

def Insert_Local_Image():
    # Local - Insert tab + Insert Local Image
    def local():
        # INSERTING LOCAL IMAGE
        NewDocument.CrtNewDoc()
        if pyautogui.click(pyautogui.locateOnScreen(f'{project_folder}/Pattern/Insert.png', confidence=0.9)) is None:
            clicker.click('Insert2')
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

        if (pyautogui.locateOnScreen(f'{project_folder}/Pattern/Images/small images/{localimage}',
                                     confidence=0.9, grayscale=True)) is None:
            with open(f'{project_folder}/Completed Tests/{day_of_test}.csv', 'a',
                      newline='') as csvfile:  # Open "Completed Tests.csv"
                writer = csv.writer(csvfile, delimiter=' ')
                writer.writerow([f"{date}', {test}, FAILED"])  # Write date, test and result
            print(f"{date}', {test}, FAILED")  # Print to console that something's wrong
        else:  # If everything's alright:
            with open(f'{project_folder}/Completed Tests/{day_of_test}.csv', 'a',
                      newline='') as csvfile:  # Open "Completed Tests.csv"
                writer = csv.writer(csvfile, delimiter=' ')
                writer.writerow([f"{date}, {test}, SUCCESS"])  # Write date, test and result
            print(f"{date}, {test}, SUCCESS")

        pyautogui.hotkey('Ctrl', 'w')
        Buttons.tab()
        Buttons.enter()
        # pyautogui.press('Enter')  # Next Line

    def CheckLocal(localimage):
        local()
        if os.name == "nt":
            pyperclip.copy(f'{project_folder}\Pattern\Images\small images\{localimage}')
        else:
            pyperclip.copy(f'{project_folder}/Pattern/Images/small images/{localimage}')
        ii()

    for localimage in Formats:
        CheckLocal(localimage)


if __name__ == "__main__":
    Insert_Local_Image()
