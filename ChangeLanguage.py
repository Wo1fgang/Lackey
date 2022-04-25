import sys
import pyautogui
import os
import Buttons
import pyperclip
import time
from datetime import datetime
import NewDocument
import NewSpreadsheet
import NewPresentation

# os.startfile("C:\\Program Files\\ONLYOFFICE\\DesktopEditors\\DesktopEditors.exe")  # Launching DesktopEditor
# time.sleep(8)

project_folder = os.getcwd()

pyautogui.PAUSE = 0.5

date = datetime.now().strftime("%d.%m.%Y %H.%M.%S")  # date = Current date in "d.m.Y H.M.S" format

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
    Buttons.tab()
    Buttons.tab()
    Buttons.tab()
    Buttons.down()
    if lang == "Chinese":
        pyautogui.typewrite('e')
    Buttons.enter()
    Buttons.tab()
    Buttons.tab()
    Buttons.tab()
    Buttons.tab()
    if os.name == "nt":
        Buttons.tab()
    Buttons.enter()


def CheckLanguage(languages):
    # Creating Document in {languages}
    NewDocument.CrtNewDoc()
    time.sleep(4)
    if (pyautogui.locateOnScreen(f'{project_folder}/Pattern/Languages/{languages}/CrDoc.png', confidence=0.9,
                                 grayscale=True)) is None:
        f = open(f'{project_folder}/Completed Tests/Tests.txt', 'a')  # Open Tests.txt
        f.write(
            f"{date} - There's a problem with {languages} language in document \n")  # Write down that something's wrong
    else:
        print(f'Everything is alright with {languages} language in document')
    pyautogui.hotkey('Ctrl', 'w')

    # Creating Spreadsheet in {languages}
    NewSpreadsheet.CrtNewSpreadsheet()
    time.sleep(4)
    if (pyautogui.locateOnScreen(f'{project_folder}/Pattern/Languages/{languages}/CrSpr.png', confidence=0.9,
                                 grayscale=True)) is None:
        f = open(f'{project_folder}/Completed Tests/Tests.txt', 'a')  # Open Tests.txt
        f.write(
            f"{date} - There's a problem with {languages} language in spreadsheet \n")  # Write down that something's wrong
    else:
        print(f'Everything is alright with {languages} language in spreadsheet')
    pyautogui.hotkey('Ctrl', 'w')

    # Creating Presentation in {languages}
    NewPresentation.CrtNewPresentation()
    time.sleep(4)
    if (pyautogui.locateOnScreen(f'{project_folder}/Pattern/Languages/{languages}/CrPre.png', confidence=0.9,
                                 grayscale=True)) is None:
        f = open(f'{project_folder}/Completed Tests/Tests.txt', 'a')  # Open Tests.txt
        f.write(f"{date} - There's a problem with {languages} language in presentation \n")  # Write down that something's wrong
    else:
        print(f'Everything is alright with {languages} language in presentation')
    pyautogui.hotkey('Ctrl', 'w')

    pyautogui.click(
        pyautogui.locateOnScreen(f'{project_folder}/Pattern/Languages/{languages}/Settings.png', confidence=0.9, grayscale=True))
    ChangeLang()


# Checking and changing to Belarusian language
if (pyautogui.locateOnScreen(f'{project_folder}/Pattern/Settings.png', confidence=0.9,
                             grayscale=True)) is None:
    print('You need to change language to english')
    sys.exit()
else:
    pyautogui.click(pyautogui.locateOnScreen(f'{project_folder}/Pattern/Settings.png', confidence=0.9, grayscale=True))
Buttons.tab()
Buttons.tab()
Buttons.tab()
Buttons.down()
pyautogui.typewrite('c')
Buttons.up()
Buttons.up()
Buttons.enter()
Buttons.tab()
Buttons.tab()
Buttons.tab()
Buttons.tab()
if os.name == "nt":
    Buttons.tab()
Buttons.enter()

for lang in languages:
    CheckLanguage(lang)
