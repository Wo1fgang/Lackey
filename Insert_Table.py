import pyautogui
import time
from datetime import datetime  # библиотека которая поможет нам найти текущее время
import Buttons  # Целиком импортируем скрипт в котором описаны все клавиши на клавиатуре которые могут понадобиться

pyautogui.PAUSE = 0.5


def Insert_Table():  # Описываем функцию
    pyautogui.click(pyautogui.locateOnScreen('Pattern\\Insert.png', confidence=0.9, grayscale=True))  # Кликаем на
    # вкладку Insert

    # INSERTING 9x9 TABLE
    pyautogui.click(
        pyautogui.locateOnScreen('Pattern\\Table.png', confidence=0.9, grayscale=True))  # Кликаем на кнопку вставки
    # таблицы
    pyautogui.click(
        pyautogui.locateOnScreen('Pattern\\InsertCustomTable.png', confidence=0.9,
                                 grayscale=True))  # Выбираем пункт "Insert Custom Table"
    pyautogui.typewrite("9")  # Количество столбцов, пишем число 9
    Buttons.tab()  # Переходим на следующее поле
    pyautogui.typewrite("9")  # Количество строк, пишем число 9
    Buttons.enter()  # Нажимаем ОК

    i = 1
    while i < 10:  # Спускаемся по таблице
        pyautogui.press('Down')
        i += 1
    Buttons.enter()  # Переходим на следующую строку

    date = datetime.now().strftime("%d.%m.%Y %H.%M.%S") # Присваиваем переменной date текущую дату в формате d.m.Y H.M.S

    if (pyautogui.locateOnScreen('Pattern\\CreatedTable.png', confidence=0.9, grayscale=True)) is None: # Если
        # созданная таблица НЕ совпадает со скриншотом корректно созданной таблицы
        pyautogui.screenshot(f'Completed Tests\\Failed\\Table\\{date}.png') # Делаем скриншот в указанной папке с
        # датой в названии
        f = open('Completed Tests\\Tests.txt', 'a') #Открывает файл Tests.txt
        f.write(f"{date} - There's a problem with inserting table \n") # Записываем что в тесте который был запущен в
        # такое-то время было что-то не так
    else:
        pyautogui.screenshot(f"Completed Tests\\Success\\Table\\{date}.png")  # Если же таблица совпадает со
        # скриншотом корректно созданной таблицы, делаем скриншот
        f = open('Completed Tests\\Tests.txt', 'a') # Открываем файл
        f.write(f"{date} - 9x9 Table inserted successfully \n") # Пишем что тест удачен


if __name__ == "__main__":
    Insert_Table()