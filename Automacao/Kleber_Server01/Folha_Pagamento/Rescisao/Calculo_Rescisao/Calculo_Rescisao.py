from repository_comuns import *
from repository_folha import *
import sys

def Redmine_105():
    try:
        GeraLog(False,"Iniciando os teste da Folha")
        if not PreparaAmbiente('108805', False, '\Folha'):
            sys.exit(1)
        if not SelecionaEmpresa(13,True,'Folha'):
            sys.exit(1)
        SelecionaPeriodo(2022,10,2022,False,True)
        if not VerificaEmpresaPeriodoSelecionado('13','10','2022'):
            sys.exit(1)
        CalcularRescisao(3,5,171)
        pyautogui.press(['enter','enter','enter'])
        pyautogui.typewrite('05102022')
        pyautogui.press('enter')
        pyautogui.typewrite('05102022')
        pyautogui.press('enter')
        pyautogui.typewrite('1')
        pyautogui.press('enter')
        time.sleep(8)
        if not ExisteImagem('C:\GitHub\Auto_TGC\Automacao\Kleber_Server01\Folha_Pagamento\Rescisao\Calculo_Rescisao\img\Redmine_101010_calculo_rescisao.png',5):
            GeraLog(False,"ERRO - Cálculo da rescisão errado")
            return False
    except:
        GeraLog(False, "Interrompido os testes sobre o cenário 100000, verificar LOG acima")
    GeraLog(False,"Terminado os teste da Folha")
    return True

#pyautogui.click(1779,29)
#SelecionaEmpresa(13,True)
Redmine_105()