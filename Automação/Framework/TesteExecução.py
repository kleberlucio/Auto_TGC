from repository_functions import *
import time
from datetime import datetime
import pyautogui

def SelecionaPeriodo(Mes):
    #Diretório atual
    DirAtu = os.getcwd()
    #Diretório onde está a imagem a ser pesquisada
    DirImg = "C:\GitHub\Auto_TGC\Automação\Framework\img"
    #Acessa diretório da imagem
    os.chdir(DirImg)
    #Pesquisa a imagem no menu principal e clica no campo
    Meses = ["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"]
    Cont = 0
    for QualMes in Meses:
        Cont = Cont + 1
        if Cont == Mes:
            if datetime.now().month == Mes:
                pyautogui.doubleClick( pyautogui.locateCenterOnScreen(QualMes+'1.png', grayscale=True, confidence=0.9) )
            else:
                pyautogui.doubleClick( pyautogui.locateCenterOnScreen(QualMes+'2.png', grayscale=True, confidence=0.9) )
    #Volta para o diretório atual.
    os.chdir(DirAtu)

pyautogui.click(1804, 14)
SelecionaEmpresa('19323')
time.sleep(1)
SelecionaPeriodo(1)

