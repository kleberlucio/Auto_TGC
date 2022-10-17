"""
O Visual Studio Code deve ser acessado como administrador
Pacotes que devem ser instalados, além dos apresentados abaixo, devido a dependências:
pip install opencv-python
"""

from repository_comuns import *

def GeraSpedFiscal(TempoConclusao):
    """"
    Criação: 27/09/2022 Última Revisão 27/09/2022 Último Autor: Kleber
    Método para realizar a geração do arquivo de SPED Fiscal da Escrita Fiscal
    TempoConclusao = informe em segundos, o tempo que leva para terminar a geração do arquivo
    """
    GeraLog(False, "Iniciado a geração do Sped Fiscal")
    pyautogui.click(815, 291)
    pyautogui.press(['alt','g','0','9'])
    time.sleep(3)
    pyautogui.press('f11')
    time.sleep(TempoConclusao)
    if not ExisteImagem('C:\\GitHub\\Auto_TGC\\Automacao\\Framework\\img\\SpedFiscalGeraldoComSucesso.png',1):
        GeraLog(False,"ERRO - A geração não concluiu da forma esperada")
        return False
    
    pyautogui.press(['enter', 'esc'])
    GeraLog(False,"Concluído a geração do Sped Fiscal")
    return True

def ApuraICMS_IPI_EFD(TempoAbertura,TempoConclusao,FicaNaTela):
    """"
    Criação: 27/09/2022 Última Revisão 27/09/2022 Último Autor: Kleber
    Método para realizar a apuração de ICMS/IPI/EFD da Escrita Fiscal
    TempoAbertura = informe em segundos, o tempo que leva para abrir a opção
    TempoConclusao = informe em segundos, o tempo que leva para terminar a apuração
    FicaNaTela = informe True se deseja permanecer com a tela aberta, caso queira realizar algum outro teste ou False, se já querer sair
    """
    GeraLog(False, "Iniciado a apuração do ICMS / IPI / EFD")
    #Clica no meio da tela
    pyautogui.click(815, 291)
    #Acessa a opção de apuração
    pyautogui.press(['alt','m','1','5'])
    #Aguarda a abertura da opção
    time.sleep(TempoAbertura)
    #Manda fazer a apuração
    pyautogui.press('f11')
    #Aguarda a apuração terminar
    time.sleep(TempoConclusao)
    #Pergunta se deseja permanecer na tela ou não para fazer mais testes.
    #No caso, está saindo da tela.
    if not FicaNaTela:
        #Saindo da opção
        pyautogui.press('esc')
        time.sleep(1)
        if not ExisteImagem('C:\\GitHub\\Auto_TGC\\Automacao\\Framework\\img\\RetornoOKparaMenuPrincipal.png',1):
            GeraLog(False,"ERRO - Ocorreu algo não esperado após a apuração")
            return False
    GeraLog(False,"Concluído a apuração do ICMS / IPI / EFD")
    return True

def QuebraApuracaoEscrita(Mes,Ano):
    """"
    Criação: 27/09/2022 Última Revisão 28/09/2022 Último Autor: Kleber
    Método para quebrar as apurações da Escrita Fiscal
    Mes = Mes selecionado. Exemplo: '04'
    Ano = Ano selecionado. Exemplo: '2017'
    """
    GeraLog(False, "Iniciado a quebra das apurações")
    pyautogui.click(815, 291)
    pyautogui.press(['alt','m','0','5'])
    time.sleep(3)
    pyautogui.press('insert')
    pyautogui.typewrite('o')
    pyautogui.press(['tab','enter'])
    pyautogui.typewrite('01'+Mes+Ano)
    pyautogui.press(['enter','enter'])
    pyautogui.typewrite('Quebrando as apurações')
    pyautogui.press('enter')
    pyautogui.typewrite('1')
    pyautogui.press(['enter','f11'])
    if not ExisteImagem('C:\\GitHub\\Auto_TGC\\Automacao\\Framework\\img\\ConfirmacaoDeQuebraApuracaoICMSIPI.png',1):
        GeraLog(False,"ERRO - Não foi apresentada tela sobre quebra de apuração")
        return False
    pyautogui.press(['s','del','s','esc'])
    pyautogui.click(815, 291)
    GeraLog(False,"Concluído a quebra das apurações")
    return True 