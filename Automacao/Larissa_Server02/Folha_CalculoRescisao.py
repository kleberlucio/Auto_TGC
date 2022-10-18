from repository_folha import *
from repository_comuns import *
import sys

def Redmine_79489():
    try:
        PreparaAmbiente('79489', False, '\Folha')
        SelecionaEmpresa(55,False,'Folha')
        SelecionaPeriodo(2022,7,2019,False,False)
        VerificaEmpresaPeriodoSelecionado('55','7','2019')
        CalcularRescisao(5, 10, 1)
        pyautogui.press('S')
        pyautogui.press('enter', 'right', 'enter')
        pyautogui.typewrite('1')
        pyautogui.press('enter')
        time.sleep(8)
        pyautogui.press('N')
        time.sleep(5)
        pyautogui.press('F11')
        pyautogui.press(['N', 'N'])
        pyautogui.press(['right', 'enter'])
        time.sleep(3)
        pyautogui.press('F9')
        time.sleep(2)
        pyautogui.hotkey('alt', 'M')
        pyautogui.typewrite('Rescisão Portaria n° 1057 I - Atual')
        pyautogui.press('F9')
        pyautogui.press('S')
        time.sleep(5)
        EmissaoRelatorios(10)

    except:
        GeraLog(False, 'Erro...')



pyautogui.click(1248,8)
EmissaoRelatorios(10)


#Redmine_79489() 
#pyautogui.click(1248,8)
#time.sleep(2)
#x, y = pyautogui.position()
#print ("Posicao atual do mouse:")
#print ("x = "+str(x)+" y = "+str(y))