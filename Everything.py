import time #Библиотека используется для приостановки выполнения скрипта (12 строка)
from NewDocument import CrtNewDoc #Импортируем функцию CrtNewDoc из скрипта NewDocument
from Insert_Tab import InsertTab #Аналогично вышенаписанному
from Insert_Table import Insert_Table #Аналогично вышенаписанному
from Insert_URL_Image import Insert_URL_Image #Аналогично вышенаписанному
from Insert_Local_Image import Insert_Local_Image #Аналогично вышенаписанному
import pyautogui #Импортируем pyautogui, главная библиотека которая используется для взаимодействия с интерфейсом
import os #Библиотека для взаимодействия с операционной системой, в данном случае - для запуска редактора (10 строка)

os.startfile("C:\\Program Files\\ONLYOFFICE\\DesktopEditors\\DesktopEditors.exe") #Запускаем редактор

time.sleep(1) #Даем команду подождать 7 секунд

CrtNewDoc() #Создаем новый документ

InsertTab() #Переходим на вкладку Insert

Insert_Table() #Вставляем таблицу 9х9

Insert_URL_Image() #Вставляем изображение по URL

Insert_Local_Image() #Вставляем локальное изображение


pyautogui.alert('Тест закончен') #Показываем сообщение что текст закончен (опционально, можно закомментить)