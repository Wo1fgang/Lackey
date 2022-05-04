import pyautogui
import os
import Buttons
import time
from datetime import datetime
import clicker
import csv
import GoFullscreen
import Change_Theme

Change_Theme.ChangeThemeToLight()

test = os.path.basename(__file__)

project_folder = os.getcwd()

pyautogui.PAUSE = 0.5

GoFullscreen.goFullScreen()

date = datetime.now().strftime("%d.%m.%Y %H.%M.%S")  # date = current date in form of dd.mm.yy hh.mm.ss

day_of_test = datetime.now().strftime("%d.%m.%Y %H")


cloudlist = ["ownCloud",
             "Seafile",
             "infomaniak kDrive",
             "Liferay",
             "Nextcloud"]

if (pyautogui.locateOnScreen(f'{project_folder}/Pattern/ConnectToCloud.png',
                             confidence=0.9, grayscale=True)) is not None:
    clicker.click("ConnectToCloud")
if (pyautogui.locateOnScreen(f'{project_folder}/Pattern/Cloud.png',
                             confidence=0.9, grayscale=True)) is not None:
    clicker.click("ConnectNow")
    clicker.click("ONLYOFFICE")

def CheckCloudList(cloud):
    Buttons.down()
    time.sleep(0.5)
    if pyautogui.locateOnScreen(f'{project_folder}/Pattern/{cloud}.png') is None:
        with open(f'{project_folder}/Completed Tests/{day_of_test}.csv', 'a', newline='') as csvfile:  # Open "Completed Tests.csv"
            writer = csv.writer(csvfile, delimiter=' ')
            writer.writerow([f"{date}', {cloud}, FAILED"])  # Write date, test and result
        print(f"{date}', {cloud}, FAILED") # Print to console that something's wrong
    else:  # If everything's alright:
        with open(f'{project_folder}/Completed Tests/{day_of_test}.csv', 'a', newline='') as csvfile:  # Open "Completed Tests.csv"
            writer = csv.writer(csvfile, delimiter=' ')
            writer.writerow([f"{date}, {cloud}, SUCCESS"])  # Write date, test and result
        print(f"{date}, {cloud}, SUCCESS")


for cloud in cloudlist:
    CheckCloudList(cloud)

Buttons.escape()
Buttons.escape()

if __name__ == "__main__":  # Fail-safe so that this script would not run when we import in into Everything.py
    CheckCloudList()
