from logging import PercentStyle
from platform import python_branch
from repository_comuns import *
import pyperclip

def InserirRescisao(TempoAbertura,TempoAberturaDaTela,CodigoEmpregado):
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
        if os.path.exists("C:\\Bancos\\report.prn"):
            os.remove("C:\\Bancos\\report.prn")
        if os.path.exists("C:\\Bancos\\report.prn"):
            GeraLog(False,"ERRO - Não foi possível excluir o arquivo Report.prn")
            return False
        GeraLog(False, 'Iniciando emissão de relatórios')
        # Clica no ícone da impressora
        pyautogui.click( pyautogui.locateCenterOnScreen('C:\\GitHub\\Auto_TGC\\Automacao\\Framework\\img\\impressora.png', confidence=0.9) ) 
        time.sleep(2)
        # Clica na opção de imprimir para arquivo
        pyautogui.click( pyautogui.locateCenterOnScreen('C:\\GitHub\\Auto_TGC\\Automacao\\Framework\\img\\imprimirParaArquivo.png', confidence=0.9) )
        time.sleep(2)
        # Clica no tipo de arquivo
        pyautogui.click( pyautogui.locateCenterOnScreen('C:\\GitHub\\Auto_TGC\\Automacao\\Framework\\img\\tipoArquivo.png', confidence=0.9) )
        # Escreve o tipo de arquivo a ser usado
        pyautogui.typewrite('arquivo para')
        pyautogui.press('enter')
        time.sleep(1)
        # Informa o diretório a ser salvo o arquivo
        pyautogui.click( pyautogui.locateCenterOnScreen('C:\\GitHub\\Auto_TGC\\Automacao\\Framework\\img\\Diretorio.png', confidence=0.9) )
        time.sleep(1)
        with pyautogui.hold('ctrl'):
            pyautogui.press('A')
        pyautogui.press('delete')
        pyautogui.typewrite('C:\\Bancos\\report.prn')
        pyautogui.press(['enter', 'enter'])
        time.sleep(TempoEmissao)
        GeraLog(False, 'Concluida geração do arquivo.')
    except:
        GeraLog(False, 'Falha na emissão do relatório.')

def ModeloRescisao(TempoAbertura):
    try:
        pyautogui.hotkey('alt', 'M')
        pyperclip.copy("Rescisão Portaria n° 1057 I - Atual")
        pyautogui.hotkey("ctrl", "v")
        PressionarTeclas('enter')
        PressionarTeclas('F9')
        PressionarTeclas('S')
        EsperarTempo(TempoAbertura)
    except:
        GeraLog(False, 'Ocorreu um erro de excessão sobre a escolha do modelo de rescisão')
