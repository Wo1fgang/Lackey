from NewDocument import CrtNewDoc
from Insert_Tab import InsertTab
from Insert_Table import Insert_Table
from Insert_URL_Image import Insert_URL_Image
from Insert_Local_Image import Insert_Local_Image
import pyautogui

CrtNewDoc()

InsertTab()

Insert_Table()

Insert_URL_Image()

Insert_Local_Image()

pyautogui.alert('Тест закончен')