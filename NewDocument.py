import pyautogui  # Импортируем pyautogui, главная библиотека которая используется для взаимодействия с интерфейсом
import time  #  Импортируем библиотеки time, она нужна для команды time.sleep
import os.path  # Библиотека которая взаимодействует с системными папками, нужна для изменения папки откуда будут
# браться скриншоты для поиска в интерфейсе

pyautogui.PAUSE = 0.5


# Create New Document
def CrtNewDoc():
    if (pyautogui.locateOnScreen('Pattern\\New Document.jpg', confidence=0.9, grayscale=True)) is None:
        pyautogui.click(pyautogui.locateOnScreen('Pattern\\MainMenu.png', confidence=0.9, grayscale=True))  # Click ONLYOFFICE
        pyautogui.click(pyautogui.locateOnScreen('Pattern\\New Document.jpg', confidence=0.9, grayscale=True))
    else:
        pyautogui.click(pyautogui.locateOnScreen('Pattern\\New Document.jpg', confidence=0.9, grayscale=True))  # New Document
    time.sleep(4)


if __name__ == "__main__":
    CrtNewDoc()

# pyautogui.screenshot('C:\\Users\\Wolfgang\\Desktop\\Onlyoffice\\Auto\\Completed tests\\700.png')  #  Take screenshot
