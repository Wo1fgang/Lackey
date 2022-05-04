import pyautogui
import os
import Buttons
import time
from datetime import datetime
import NewDocument
import NewSpreadsheet
import NewPresentation
import csv
import clicker
import Change_Theme
import GoFullscreen

Change_Theme.ChangeThemeToLight()

GoFullscreen.goFullScreen()

# os.startfile("C:\\Program Files\\ONLYOFFICE\\DesktopEditors\\DesktopEditors.exe")  # Launching DesktopEditor
# time.sleep(8)

project_folder = os.getcwd()

pyautogui.PAUSE = 0.5

date = datetime.now().strftime("%d.%m.%Y %H.%M.%S")  # date = Current date in "d.m.Y H.M.S" format

test = os.path.basename(__file__)  # name of this script = variable "test". Used for easy reading the csv with results.

day_of_test = datetime.now().strftime("%d.%m.%Y %H")

languages = [
    "Belarusian",
    "Bulgarian",
    "Catalan",
    "Czech",
    "Danish",
    "German",
    "Greek",
    "English",
    "Spanish",
    "Finnish",
    "French",
    "Galician",
    "Hungarian",
    "Indonesian",
    "Italian",
    "Japanese",
    "Korean",
    "Lao",
    "Latvian",
    "Netherlands",
    "Norwegian",
    "Polish",
    "Portuguese",
    "Romanian",
    "Russian",
    "Slovak",
    "Slovenian",
    "Swedish",
    "Turkish",
    "Ukrainian",
    "Vietnamese",
    "Chinese"
]


def ChangeLang():
    for _ in range(3):
        pyautogui.press('Tab')
    Buttons.down()
    if lang == "Chinese":
        pyautogui.typewrite('e')
    Buttons.enter()
    for _ in range(4):
        pyautogui.press('Tab')
    if os.name == "nt":
        Buttons.tab()
    Buttons.enter()


def CheckLanguage(languages):
    # Creating Document in {languages}
    NewDocument.CrtNewDoc()
    time.sleep(4)
    if (pyautogui.locateOnScreen(f'{project_folder}/Pattern/Languages/{languages}/CrDoc.png', confidence=0.9,
                                 grayscale=True)) is None:
        with open('Completed Tests.csv', 'a', newline='') as csvfile:  # Open "Completed Tests.csv"
            writer = csv.writer(csvfile, delimiter=' ')
            writer.writerow([f"{date}', {languages} Document, FAILED"])  # Write date, test and result
        print(f"{date}', {languages} Document, FAILED")  # Print to console that something's wrong
    else:
        print(f'Everything is alright with {languages} language in document')
    pyautogui.hotkey('Ctrl', 'w')
    clicker.click('MainMenu')

    # Creating Spreadsheet in {languages}
    NewSpreadsheet.CrtNewSpreadsheet()
    time.sleep(4)
    if (pyautogui.locateOnScreen(f'{project_folder}/Pattern/Languages/{languages}/CrSpr.png', confidence=0.9,
                                 grayscale=True)) is None:
        with open('Completed Tests.csv', 'a', newline='') as csvfile:  # Open "Completed Tests.csv"
            writer = csv.writer(csvfile, delimiter=' ')
            writer.writerow([f"{date}',{languages} Spreadsheet, FAILED"])  # Write date, test and result
        print(f"{date}', {languages} Spreadsheet, FAILED")  # Print to console that something's wrong
    else:
        print(f'Everything is alright with {languages} language in spreadsheet')
    pyautogui.hotkey('Ctrl', 'w')
    clicker.click('MainMenu')

    # Creating Presentation in {languages}
    NewPresentation.CrtNewPresentation()
    time.sleep(4)
    if (pyautogui.locateOnScreen(f'{project_folder}/Pattern/Languages/{languages}/CrPre.png', confidence=0.9,
                                 grayscale=True)) is None:
        with open('Completed Tests.csv', 'a', newline='') as csvfile:  # Open "Completed Tests.csv"
            writer = csv.writer(csvfile, delimiter=' ')
            writer.writerow([f"{date}',{languages} Presentation, FAILED"])  # Write date, test and result
        print(f"{date}', {languages} Presentation, FAILED")  # Print to console that something's wrong
    else:
        print(f'Everything is alright with {languages} language in presentation')
    pyautogui.hotkey('Ctrl', 'w')
    clicker.click('MainMenu')

    pyautogui.click(
        pyautogui.locateOnScreen(f'{project_folder}/Pattern/Languages/{languages}/Settings.png', confidence=0.9, grayscale=True))
    ChangeLang()


    # Checking and changing to Belarusian language
    if (pyautogui.locateOnScreen(f'{project_folder}/Pattern/Settings.png', confidence=0.9,
                                 grayscale=True)) is None:
        pyautogui.click(pyautogui.locateOnScreen(f'{project_folder}/Pattern/MainMenu.png', confidence=0.9, grayscale=True))
    else:
        pyautogui.click(pyautogui.locateOnScreen(f'{project_folder}/Pattern/Settings.png', confidence=0.9, grayscale=True))
    for _ in range(3):
        pyautogui.press('Tab')
    Buttons.down()
    pyautogui.typewrite('c')
    for _ in range(2):
        pyautogui.press('up')
    Buttons.enter()
    for _ in range(4):
        pyautogui.press('Tab')
    if os.name == "nt":
        Buttons.tab()
    Buttons.enter()

for lang in languages:
    CheckLanguage(lang)
