from platform import python_branch
from repository_comuns import *

def CalcularRescisao(TempoAbertura,TempoAberturaDaTela,CodigoEmpregado):
    try:
        GeraLog(False, "Iniciando o cálculo de rescisão")
        #Clica no meio da tela
        pyautogui.click(815, 291)
        #Acessa a opção de cálculo da rescisão
        pyautogui.press(['alt','e','0', '1'])
        #Aguarda a abertura da opção
        time.sleep(TempoAbertura)
        pyautogui.press('insert')
        time.sleep(TempoAberturaDaTela)
        pyautogui.typewrite(str(CodigoEmpregado))
        pyautogui.press('enter')
        GeraLog(False, "Concluído o método CalcularRescisão")
    except:
        GeraLog(False,'Ocorreu um erro no método CalcularRescisão')

def EmissaoRelatorios(TempoEmissao):
    try:
        #Excluindo relatórios gerados pelo sistema
        if os.path.exists("C:\\Users\\Public\\Documents\\Report.prn"):
            os.remove("C:\\Users\\Public\\Documents\\Report.prn")
        if os.path.exists("C:\\Users\\Public\\Documents\\Report.prn"):
            GeraLog(False,"ERRO - Não foi possível excluir o arquivo Report.prn")
            return False
        GeraLog(False, 'Iniciando emissão de relatórios e recibos')
        # clica no ícone da impressora
        pyautogui.click( pyautogui.locateCenterOnScreen('C:\GitHub\Auto_TGC\Automacao\Framework\img\impressora.png', confidence=0.9) ) 
        time.sleep(1)
        # clica na opção de imprimir para arquivo
        pyautogui.click( pyautogui.locateCenterOnScreen('C:\GitHub\Auto_TGC\Automacao\Framework\img\imprimirParaArquivo.png', confidence=0.9) )
        time.sleep(2)
        # clica no tipo de arquivo
        #GeraLog(False, 'Não chegou a clicar no tipo de arquivo')
        #pyautogui.press('tab')
        pyautogui.click( pyautogui.locateCenterOnScreen('C:\GitHub\Auto_TGC\Automacao\Framework\img\tipoArquivo.png', confidence=0.9) )
        GeraLog(False, 'clicou no tipo de arquivo')
        # escreve o tipo de arquivo a ser usado
        #GeraLog(False, 'Vai começar a digitar')
        pyautogui.typewrite('arquivo para')
        #GeraLog(False, 'digitou o arquivo')
        # clica na geração do arquivo
        pyautogui.click( pyautogui.locateCenterOnScreen('C:\GitHub\Auto_TGC\Automacao\Framework\img\geracaoRelatorio.png', confidence=0.9) )
        time.sleep(TempoEmissao)
    except:
        GeraLog(False, 'Falha na emissão do relatório.')
