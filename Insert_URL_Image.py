import pyautogui  # Importing pyautogui, the most important library in those scripts
import pyperclip  # interaction with clipboard
from datetime import datetime  # Get current time
import Buttons  # Script to easily tell which buttons to press (pyautogui.press still can be used)
import time  # Used to "pause" execution of script
import os  # Interaction with operational system
import c  # Script c.py, to easily click on any button from screenshot and stop the script if it can't find that button
import csv  # Export results into csv
import sys  # Interaction with scripts (in that case, sys.exit, to stop execution of script if something is wrong
import GoFullscreen  # Script that enables full-screen on OO Editor, just in case
import NewDocument  # Script that creates new document

test = os.path.basename(__file__)  # name of this script = variable "test". Used for easy reading the csv with results.

pyautogui.PAUSE = 0.8  # pausing every interaction with pyautogui for 0.8 seconds

project_folder = os.getcwd()  # used in pointing where to look for screenshots and save results (folder of this project)

GoFullscreen.goFullScreen()  # fail-safe in case OO Editor is not in full-screen

date = datetime.now().strftime("%d.%m.%Y %H.%M.%S")  # date = current date in form of dd.mm.yy hh.mm.ss

def Insert_URL_Image():  # creating function
    NewDocument.CrtNewDoc()  # Creating new document
    pyautogui.press('alt')  # Pressing "alt" to get into shortcut mode (that's just easier)
    pyautogui.press('i')  # Going into "Insert" tab
    pyautogui.press('e')  # Choosing "Image"
    Buttons.down()
    Buttons.down()  # Choosing insert from URL
    Buttons.enter()  # Pressing OK
    pyperclip.copy('https://i.redd.it/or438ov4zno81.jpg')  # Copying URL with image
    pyautogui.hotkey('Ctrl', 'v')  # Pasting just copied URL
    Buttons.enter()  # Inserting
    if (pyautogui.locateOnScreen(f'{project_folder}/Pattern/ErrorURL.png', confidence=0.8)) is not None:
        # If for some reason we see error message in URL field:

        Buttons.escape()  # Closing the URL window
        pyautogui.hotkey('Ctrl', 'w')  # Closing the document

        with open('Completed Tests.csv', 'a', newline='') as csvfile:  # Open "Completed Tests.csv"
            writer = csv.writer(csvfile, delimiter=' ')
            writer.writerow([f"{date}', Inserting URL, FAILED"])  # Write date, test and result
        print("There's a problem with inserting image from URL")  # Print to console that something's wrong

    else:  # If everything is ok and we inserted the image from URL
        Buttons.escape()  # Escaping from just inserted image
        pyautogui.hotkey('Ctrl', 'w')  # Closing the document
        Buttons.tab()  # In opened "save the changes" window switch to "No"
        Buttons.enter()  # Press enter

        if (pyautogui.locateOnScreen(f'{project_folder}/Pattern/InsertedURLImage.png',
                                     confidence=0.9, grayscale=True)) is None:
            # If our inserted image is not the same as we expected:

            pyautogui.screenshot(f'{project_folder}/Completed Tests/Failed/Image/URL/{date}.png')
            # Screenshot to see what's wrong

            with open('Completed Tests.csv', 'a', newline='') as csvfile:  # Open "Completed Tests.csv"
                writer = csv.writer(csvfile, delimiter=' ')
                writer.writerow([f"{date}', {test}, FAILED"])  # Write date, test and result
            print("There's a problem with inserting image from URL") # Print to console that something's wrong
        else:  # If everything's alright:
            with open('Completed Tests.csv', 'a', newline='') as csvfile:  # Open "Completed Tests.csv"
                writer = csv.writer(csvfile, delimiter=' ')
                writer.writerow([f"{date}, {test}, SUCCESS"])  # Write date, test and result


if __name__ == "__main__":  # Fail-safe so that this script would not run when we import in into Everything.py
    Insert_URL_Image()