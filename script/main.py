import pandas as pd 
import time
import pyautogui

pyautogui.PAUSE = 0.5
time.sleep(1)
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)

pyautogui.click(x=1067, y=64)
pyautogui.write('http://127.0.0.1:5500/index.html')
pyautogui.press('enter')
pyautogui.click(x=727, y=569)
pyautogui.write('admin')
pyautogui.press('tab')
pyautogui.write('123')
time.sleep(1)
pyautogui.press('tab')  
pyautogui.press('enter')

tabela = pd.read_csv('planilha.csv')
time.sleep(3)

for i in tabela.index :

    pyautogui.click(x=693, y=495)
    usuario_nome = tabela.loc[i, 'Nome']
    pyautogui.write(usuario_nome)
    pyautogui.press('tab')
    time.sleep(1)

    usuario_email = tabela.loc[i, 'Email']
    pyautogui.write(usuario_email)
    pyautogui.press('tab')
    time.sleep(1)

    usuario_endereco = tabela.loc[i, 'Endereco']
    pyautogui.write(usuario_endereco)
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(1)





