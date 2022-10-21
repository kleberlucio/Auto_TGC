from repository_folha import *
from repository_comuns import *

def Redmine_79489():
    try:
        PreparaAmbiente('79489', False, '\Folha')
        SelecionaEmpresa(55,False,'Folha')
        SelecionaPeriodo(2022,7,2019,False,False)
        VerificaEmpresaPeriodoSelecionado('55','7','2019')
        InserirRescisao(5, 5, 1)
        EsperarTempo(2)
        # Marcando sim em buscar datas do aviso prévio
        PressionarTeclas('S')
        # Selecionando sim em calcular aviso lei 12.506
        pyautogui.press(['enter', 'right', 'enter'])
        # Informando o tipo de rescisão
        pyautogui.press(['enter', 'enter', 'enter'])
        EscreverTexto('1')
        PressionarTeclas('enter')
        EsperarTempo(8)
        # Marcando para sim retirar os dias de aviso excedentes no cálculo
        PressionarTeclas('S')
        EsperarTempo(5)
        # Gravando a rescisão
        pyautogui.press(['F11', 'N', 'N', 'right', 'enter'])
        EsperarTempo(3)
        # Conferindo se a rescisão foi salva
        ExisteImagem('C:\\GitHub\\Auto_TGC\\Automacao\\Larissa_Server02\\Arquivos_Folha\\79489\\rescisaoSalva.png', 3)
        # Iniciando a emissão da rescisão
        PressionarTeclas('F9')
        EsperarTempo(2)
        ModeloRescisao(5)
        EmissaoRelatorios(10)
        ComparaArquivo('C:\\GitHub\\Auto_TGC\\Automacao\\Larissa_Server02\\Arquivos_Folha\\79489\\Rescisão.prn', 
        'C:\\Bancos\\report.prn', 'C:\\GitHub\Auto_TGC\\Automacao\\Larissa_Server02\\Arquivos_Folha\\79489\\erroRescisão.txt')
        PressionarTeclas(['esc','S'])
        EsperarTempo(3)
        EmissaoRelatorios(10)
        ComparaArquivo('C:\\GitHub\\Auto_TGC\\Automacao\\Larissa_Server02\\Arquivos_Folha\\79489\\TermoRescisão.prn', 
        'C:\\Bancos\\report.prn', 'C:\\GitHub\Auto_TGC\\Automacao\\Larissa_Server02\\Arquivos_Folha\\79489\\erroTermo.txt')
        GeraLog(False, 'Concluido redmine 79489 com sucesso.')
    except:
        GeraLog(False, 'Erro no redmine 79489.')


def Redmine_100279():
    try:
        PreparaAmbiente('100279', False, '\Folha')
        SelecionaEmpresa(55,False,'Folha')
        SelecionaPeriodo(2022,2,2021,False,False)
        VerificaEmpresaPeriodoSelecionado('55','2','2021')
        InserirRescisao(5, 5, 24)
        EsperarTempo(2)
        # Marcando para não buscar a data do aviso
        PressionarTeclas('N')
        PressionarTeclas(['enter', 'enter', 'enter', 'enter'])
        # Preenchendo a data da rescisão
        EscreverTexto('15022021')
        # Marcando para retirar os dias de afastamento 
        PressionarTeclas(['enter', 'S'])
        EscreverTexto('3')
        PressionarTeclas('enter')
        EsperarTempo(10)
        # Abrindo a tela do cálculo das férias
        pyautogui.hotkey("alt", "F")
        # Conferindo se o cálculo das férias está correto
        ExisteImagem('C:\\GitHub\\Auto_TGC\\Automacao\\Larissa_Server02\\Arquivos_Folha\\100279\\ferias.png')
        # Salvando a rescisão
        PressionarTeclas(['F11', 'enter'])
        # Preenchendo a data de homologação da rescisão
        EscreverTexto('15022021')
        PressionarTeclas(['F11', 'N', 'N', 'right', 'enter'])
        # Conferindo se a rescisão foi salva na grid
        ExisteImagem('C:\\GitHub\\Auto_TGC\\Automacao\\Larissa_Server02\\Arquivos_Folha\\100279\\RescisaoSalva.png')
        PressionarTeclas('F9')
        EsperarTempo(2)
        ModeloRescisao(5)
        EmissaoRelatorios(10)
        # Comparando o arquivo de rescisão
        ComparaArquivo('C:\\GitHub\\Auto_TGC\\Automacao\\Larissa_Server02\\Arquivos_Folha\\100279\\Rescisão.prn', 
        'C:\\Bancos\\report.prn', 'C:\\GitHub\Auto_TGC\\Automacao\\Larissa_Server02\\Arquivos_Folha\\100279\\erroRescisão.txt')
        PressionarTeclas(['esc','S'])
        EsperarTempo(3)
        EmissaoRelatorios(10)
        # Comparando o termo de rescisão
        ComparaArquivo('C:\\GitHub\\Auto_TGC\\Automacao\\Larissa_Server02\\Arquivos_Folha\\100279\\TermoRescisão.prn', 
        'C:\\Bancos\\report.prn', 'C:\\GitHub\Auto_TGC\\Automacao\\Larissa_Server02\\Arquivos_Folha\\100279\\erroTermo.txt')
        GeraLog(False, 'Concluido redmine 100279 com sucesso.')
    except:
        GeraLog(False, 'Erro no redmine 100279.')


#pyautogui.click(1248,8)
#time.sleep(2)

Redmine_100279()