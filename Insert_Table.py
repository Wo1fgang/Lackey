import pyautogui
import time
from datetime import datetime
import Buttons

pyautogui.PAUSE = 0.5


def Insert_Table():
    pyautogui.click(pyautogui.locateOnScreen('Pattern\\Insert.png', confidence=0.9, grayscale=True))  # Click on Insert
    time.sleep(0.5)
    pyautogui.click(pyautogui.locateOnScreen('Pattern\\Insert.png', confidence=0.9, grayscale=True))  # Click on Insert

    # INSERTING 9x9 TABLE
    pyautogui.click(pyautogui.locateOnScreen('Pattern\\Table.png', confidence=0.9, grayscale=True))  # Click on Insert Table
    pyautogui.click(
        pyautogui.locateOnScreen('Pattern\\InsertCustomTable.png', confidence=0.9, grayscale=True))  # Click Insert Custom Table
    pyautogui.typewrite("9")  # Number of columns
    Buttons.tab()  # Next textbox
    pyautogui.typewrite("9")  # Number of Rows
    Buttons.enter()  # OK

    i = 1
    while i < 10:  # Down the table we go
        pyautogui.press('Down')
        i += 1
    Buttons.enter()  # Next Line

    date = datetime.now().strftime("%d.%m.%Y %H.%M.%S")

    if (pyautogui.locateOnScreen('Pattern\\CreatedTable.png', confidence=0.9, grayscale=True)) is None:
        pyautogui.screenshot(f'Completed Tests\\Failed\\Table\\{date}.png')
        f = open('Completed Tests\\Tests.txt', 'a')
        f.write(f"{date} - There's a problem with inserting table \n")
    else:
        pyautogui.screenshot(f"Completed Tests\\Success\\Table\\{date}.png")
        f = open('Completed Tests\\Tests.txt', 'a')
        f.write(f"{date} - 9x9 Table inserted successfully \n")


if __name__ == "__main__":
    Insert_Table()