from platform import python_branch
from repository_comuns import *

def CalcularRescisao(TempoAbertura,TempoAberturaDaTela,CodigoEmpregado):
    try:
        GeraLog(False, "Iniciando o cálculo de rescisão")
        #Clica no meio da tela
        pyautogui.click(815, 291)
        #Acessa a opção de cálculo da rescisão
        pyautogui.press(['alt','e','0','1'])
        #Aguarda a abertura da opção
        time.sleep(TempoAbertura)
        pyautogui.press('insert')
        time.sleep(TempoAberturaDaTela)
        pyautogui.typewrite(str(CodigoEmpregado))
        pyautogui.press('enter')
        GeraLog(False, "Concluído o método CalcularRescisão")
    except:
        GeraLog(False,'Ocorreu um erro no método CalcularRescisão')

def AvisoLei12506(GeraAviso, ProjetaData):
    try:
        GeraLog(False, 'Selecionando o aviso 12506 na rescisão')
        pyautogui.press('enter')
        if GeraAviso == 'S':
            pyautogui.press('enter')
        else:
            pyautogui.press(['left', 'enter'])
        if GeraAviso == 'S' and ProjetaData == 'S':
            pyautogui.press('right')
    except:
        GeraLog(False, 'Erro no aviso da lei 12506.')