import pyautogui
from time import sleep

buttom = pyautogui.confirm(text='Do you want to clean up temporary files?', title='Clear', buttons=['Yes', 'No'])

pyautogui.PAUSE = 0.5

if buttom == 'Yes':
    pyautogui.alert('do not touch the mouse or keyboard. ')
    pyautogui.hotkey('winleft','r')
    pyautogui.write('%temp%')
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('shift','del')
    pyautogui.hotkey('alt', 'f4')
    sleep(1)
    pyautogui.hotkey('winleft', 'r')
    pyautogui.write('temp')
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('shift','del')
    pyautogui.hotkey('alt', 'f4')
pyautogui.alert(text='Finished', title='Alert', button='OK')