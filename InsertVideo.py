import pyautogui
import time
import os.path
import pyperclip  # Library for copypasting stuff
from datetime import datetime
import Buttons
import GoFullscreen
import clicker
import csv
import NewPresentation
import Change_Theme

Change_Theme.ChangeThemeToLight()

GoFullscreen.goFullScreen()

pyautogui.PAUSE = 0.7

project_folder = os.getcwd()

test = os.path.basename(__file__)

day_of_test = datetime.now().strftime("%d.%m.%Y %H")

def InsertVideo():
    NewPresentation.CrtNewPresentation()
    pyautogui.press("alt")
    pyautogui.press("i")
    clicker.click("Video")
    if os.name == "nt":
        pyperclip.copy(f'{project_folder}\Pattern\ video.mp4')
    else:
        pyperclip.copy(f'{project_folder}/Pattern/video.mp4')
    pyautogui.hotkey("ctrl", "v")
    Buttons.enter()
    pyautogui.click(pyautogui.locateOnScreen(f'{project_folder}/Pattern/InsertedVideo.png', confidence=0.9))
    clicker.click("InsertedVideo")
    time.sleep(1)

    date = datetime.now().strftime("%d.%m.%Y %H.%M.%S")

    if (pyautogui.locateOnScreen(f'{project_folder}/Pattern/CorrectVideo.png',
                                 confidence=0.9, grayscale=True)) is None:
        with open(f'{project_folder}/Completed Tests/{day_of_test}.csv', 'a', newline='') as csvfile:  # Open "Completed Tests.csv"
            writer = csv.writer(csvfile, delimiter=' ')
            writer.writerow([f"{date}', {test}, FAILED"])  # Write date, test and result
        print(f"{date}', {test}, FAILED") # Print to console that something's wrong
    else:  # If everything's alright:
        with open(f'{project_folder}/Completed Tests/{day_of_test}.csv', 'a', newline='') as csvfile:  # Open "Completed Tests.csv"
            writer = csv.writer(csvfile, delimiter=' ')
            writer.writerow([f"{date}, {test}, SUCCESS"])  # Write date, test and result
        print(f"{date}, {test}, SUCCESS")


if __name__ == "__main__":
    InsertVideo()