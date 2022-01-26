import pyautogui
import time
import os.path

pyautogui.PAUSE = 0.5

os.chdir('C:\\Auto')


# Create New Document
def CrtNewDoc():
    if (pyautogui.locateOnScreen('New Document.jpg', confidence=0.9, grayscale=True)) is None:
        pyautogui.click(pyautogui.locateOnScreen('MainMenu.png', confidence=0.9, grayscale=True))  # Click ONLYOFFICE
        pyautogui.click(pyautogui.locateOnScreen('New Document.jpg', confidence=0.9, grayscale=True))
    else:
        pyautogui.click(pyautogui.locateOnScreen('New Document.jpg', confidence=0.9, grayscale=True))  # New Document
    time.sleep(4)


if __name__ == "__main__":
    CrtNewDoc()

# pyautogui.screenshot('C:\\Users\\Wolfgang\\Desktop\\Onlyoffice\\Auto\\Completed tests\\700.png')  #  Take screenshot
