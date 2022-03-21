import time # Used for time.sleep command, to "pause" execution of code
from NewDocument import CrtNewDoc
from Insert_Tab import InsertTab
from Insert_Table import Insert_Table
from Insert_URL_Image import Insert_URL_Image
from Insert_Local_Image import Insert_Local_Image #All above: importing scripts to run from this one script
import pyautogui # Main library to interact with UI
import os # Library used to launch desktop

os.startfile("C:\\Program Files\\ONLYOFFICE\\DesktopEditors\\DesktopEditors.exe") # Launching desktopeditor

time.sleep(8) # Wait 8 seconds

CrtNewDoc() # Creating new document

InsertTab() # Click on "Insert" tab

Insert_Table() # Inserting 9x9 table

Insert_URL_Image() # Inserting image from URL

Insert_Local_Image() # Inserting local images


pyautogui.alert('Тест закончен. Результаты можно посмотреть в C:\Lackey\Completed Tests\Tests.txt') # Message that test is done