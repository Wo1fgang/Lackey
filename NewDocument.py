import pyautogui  # Импортируем pyautogui, главная библиотека которая используется для взаимодействия с интерфейсом
import time  # Импортируем библиотеки time, она нужна для команды time.sleep

pyautogui.PAUSE = 0.5  # Устанавливаем паузу в полсекунды при любом обращении к pyautogui, нужно на всякий случай
# когда интерфейс редактора не успевает прогрузиться


def CrtNewDoc():  # описываем функцию CrtNewDoc
    if (pyautogui.locateOnScreen('Pattern\\New Document.jpg', confidence=0.9,
                                 grayscale=True)) is None:  # если скрипт не может найти кнопку "Создать новый документ"
        pyautogui.click(
            pyautogui.locateOnScreen('Pattern\\MainMenu.png', confidence=0.9,
                                     grayscale=True))  # То он кликает на кнопку чтобы перейти в главное меню
        pyautogui.click(pyautogui.locateOnScreen('Pattern\\New Document.jpg', confidence=0.9,
                                                 grayscale=True))  # и создает новый документ
    else:
        pyautogui.click(
            pyautogui.locateOnScreen('Pattern\\New Document.jpg', confidence=0.9,
                                     grayscale=True))  # если он уже в главном меню, создает новый документ
    time.sleep(4)  # Ждет 4 секунды чтобы документ успел прогрузиться


if __name__ == "__main__":
    CrtNewDoc()  # fail-safe чтобы скрипт не вызывался когда его импортируют
