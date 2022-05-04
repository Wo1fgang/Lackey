import time  # Used for time.sleep command, to "pause" execution of code
import ChangeUserName
from Insert_Table import Insert_Table
from URL_Image_Document import Insert_URL_Image_DOC
from URL_Image_Spreadsheet import Insert_URL_Image_SPR
from URL_Image_Presentation import Insert_URL_Image_PRE
import Check_cloud_page
from Insert_Local_Image import Insert_Local_Image  # All above: importing scripts to run from this one script
import pyautogui  # Main library to interact with UI
import os  # Library used to launch desktop
from datetime import datetime

test = os.path.basename(__file__)

day_of_test = datetime.now().strftime("%d.%m.%Y %H")

# if os.name != "nt":
#     os.startfile("C:\\Program Files\\ONLYOFFICE\\DesktopEditors\\DesktopEditors.exe") # Launching desktop editor
#     time.sleep(8)  # Wait 8 seconds

Check_cloud_page

Insert_Table()  # Inserting 9x9 table

Insert_URL_Image_DOC()  # Inserting image from URL

Insert_URL_Image_SPR()  # Inserting image from URL

Insert_URL_Image_PRE()  # Inserting image from URL

if os.name != "nt":
    Insert_Local_Image()  # Inserting local images

ChangeUserName.CheckUsername()  # Checking if changing username works


pyautogui.alert(f'Testing is done, see results in: /Completed Tests/{day_of_test}.csv')  # Message that test is done