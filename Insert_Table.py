import pyautogui
import time
from datetime import datetime  # Library used to get current time
import Buttons  # Importing Buttons.py to quickly use necessary buttonpresses

pyautogui.PAUSE = 0.5

time.sleep(2)

def Insert_Table():  # defining function so we can import it into Everything.py
    # pyautogui.click(pyautogui.locateOnScreen('Pattern\\Insert.png', confidence=0.9, grayscale=True))  # Click on "Insert" tab
    #
    # # INSERTING 9x9 TABLE
    # pyautogui.click(pyautogui.locateOnScreen('Pattern\\Table.png', confidence=0.9, grayscale=True))  # Insert table
    # pyautogui.click(pyautogui.locateOnScreen('Pattern\\InsertCustomTable.png', confidence=0.9, grayscale=True))  # "Insert Custom Table"
    pyautogui.press('alt')
    pyautogui.press('i')
    pyautogui.press('d')
    Buttons.down()
    Buttons.enter()
    pyautogui.typewrite("9")  # Number of columns (9)
    Buttons.tab()  # Next field
    pyautogui.typewrite("9")  # Number of rows (9)
    Buttons.enter()  # Press ОК

    i = 1
    while i < 10:  # Moving down the table
        pyautogui.press('Down')
        i += 1
    Buttons.enter()  # Next line

    date = datetime.now().strftime("%d.%m.%Y %H.%M.%S") # date = Current date in "d.m.Y H.M.S" format

    if (pyautogui.locateOnScreen('Pattern\\CreatedTable.png', confidence=0.9, grayscale=True)) is None: # If we can't locate created table, if something's gone wrong
        pyautogui.screenshot(f'Completed Tests\\Failed\\Table\\{date}.png') # We take screenshot with date in name
        f = open('Completed Tests\\Tests.txt', 'a') # Open Tests.txt
        f.write(f"{date} - There's a problem with inserting table \n") # Write down that something's wrong
    else:
        pyautogui.screenshot(f"Completed Tests\\Success\\Table\\{date}.png")
        f = open('Completed Tests\\Tests.txt', 'a')
        f.write(f"{date} - 9x9 Table inserted successfully \n") # Same if everything is alright


if __name__ == "__main__":
    Insert_Table()