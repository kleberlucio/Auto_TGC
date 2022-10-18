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
        AvisoLei12506('S', 'N')
        
# Informando as datas de aviso e data de rescisão
        pyautogui.write('06062019', 'enter', '28072019', 'enter')
# Informando o motivo de rescisão
        pyautogui.press('1', 'enter')
        time.sleep(5)
# Gravando a rescisão
        pyautogui.press('enter', 'F11', 'right', 'enter', 'right', 'enter')


    except:
        GeraLog(False, 'Erro...')


Redmine_79489() 

#pyautogui.click(1248,8)

#time.sleep(2)
#x, y = pyautogui.position()
#print ("Posicao atual do mouse:")
#print ("x = "+str(x)+" y = "+str(y))