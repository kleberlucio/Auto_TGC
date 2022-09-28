"""
O Visual Studio Code deve ser acessado como administrador
Pacotes que devem ser instalados, além dos apresentados abaixo, devido a dependências:
pip install opencv-python
"""

from datetime import datetime
from operator import truediv
from winreg import *
import winreg
import os
import psutil
import patoolib
import glob
import time
import pyautogui
import logging
import sys

def ExisteImagem(Imagem):
    DirAtu = os.getcwd()
    #Diretório onde está a imagem a ser pesquisada
    DirImg = "C:\GitHub\Auto_TGC\Automacao\Framework\img"
    #Acessa diretório da imagem
    os.chdir(DirImg)
    time.sleep(1)
    if not ( pyautogui.locateCenterOnScreen(Imagem, confidence=0.9) ):
        os.chdir(DirAtu)
        return False
    else:
        os.chdir(DirAtu)
        return True

def VerificaEmpresaPeriodoSelecionado(Empresa,Mes,Ano):
    """
    Criação: 28/09/2022 Última Revisão 28/09/2022 Último Autor: Kleber
    Empresa = Informe o código da empresa selecionada. Exemplo: '10'
    Mes = Informe o mês selecionado. Exemplo: '5'
    Ano = Informe o ano selecionado. Exemplo: '2020'
    """    
    GeraLog(False,"Iniciado a verificação da empresa, mês e ano selecionado")
    aReg = winreg.ConnectRegistry(None,HKEY_CURRENT_USER)
    aKey = winreg.OpenKey(aReg,r"SOFTWARE\Tron\Selecionado")
    Passou = True
    try:
        i = 0
        while 1:
            name, value, type = EnumValue(aKey, i)
            if name == 'Codigo' and not (Empresa == value):
                GeraLog(False,"ERRO - Não selecionou a empresa correta")
                Passou = False
                break
            if name == 'Mes' and not (Mes == value):
                GeraLog(False,"ERRO - Não selecionou o mês correto")
                Passou = False
                break
            if name == 'Ano' and not (Ano == value):
                GeraLog(False,"ERRO - Não selecionou o ano correto")
                Passou = False
                break
            i += 1
    except WindowsError:
        GeraLog(False,"Finalizada a verificação da empresa, mês e ano selecionado")
    CloseKey(aKey)
    return Passou

def ComparaArquivo(Arq1,Arq2,ArqDif):
    """
    Criação: 27/09/2022 Última Revisão 27/09/2022 Último Autor: Kleber
    Arq1 = Caminho e nome do arquivo que está guardado. Exemplo: "C:/GitHub/Auto_TGC/Automacao/Escrita_Fiscal/Geracao_De_Informacoes_Oficiais/SPED_Fiscal/108805/Origem.txt" 
    Arq2 = Caminho e nome do arquivo de origem. Exemplo: "C:/Users/Desenvolvedor/Documents/Report.txt" 
    ArqDif = Caminho e nome do arquivo que vai demonstrar as diferenças. Exemplo: "C:\\GitHub\\Auto_TGC\\Automacao\\Escrita_Fiscal\\Geracao_De_Informacoes_Oficiais\\SPED_Fiscal\\108805\\Difer.txt"     
    """    
    GeraLog(False,"Iniciado a comparação de arquivos")
    #Cria o arquivo que vai demostrar as diferenças
    flog = open(ArqDif, "w")
    #Abre o arquivo que fica guardado
    f1 = open(Arq1, "r", encoding ="utf8")  
    #Abre o arquivo que foi gerado agora
    f2 = open(Arq2, "r", encoding ="utf8")          
    i = 0
    #Inicia a variável TemDif como falso. Ela dirá se tem diferença ou não
    TemDif = False
    #Inicia a leitura dos dois arquivos para ver se há diferença
    for line1 in f1:
        i += 1
        for line2 in f2:
            if line1 == line2:
                break
            else:
                TemDif = True
                flog.write('Diferença na linha ' + str(i) + ':\n')
                flog.write('Antes  : ' + line1)
                flog.write('Depois: ' + line2)
                break
    #Fecha todos arquivos manipulados
    f1.close()                                       
    f2.close()
    flog.close()
    #Se tiver encontrado diferença, vai criar no LOG geral a linha abaixo, pedindo para ir no LOG de diferença para ver o que houve.
    if TemDif:
       GeraLog(False,"ERRO - O arquivo está diferente. Favor consultar " + ArqDif)
       return False
    GeraLog(False,"Concluído a comparação de arquivos")
    return True

def SelecionaEmpresa(CodigoEmpresa,TelaCertificado):
    """
    Criação: 27/09/2022 Última Revisão 27/09/2022 Último Autor: Kleber
    CodigoEmpresa = Informe o código da empresa a ser selecionada. Exemplo: 21
    TelaCertificado = Após informar o código da empresa, pode ser que apareça a tela de certificados
                      vencidos. Informe True para dar um ESC nesta tela ou False caso o seu ambiente
                      de teste não apareça essa tela.
    """
    GeraLog(False,"Iniciado a Seleção da empresa")
    #Diretório atual
    DirAtu = os.getcwd()
    #Diretório onde está a imagem a ser pesquisada
    DirImg = "C:\GitHub\Auto_TGC\Automacao\Framework\img"
    #Acessa diretório da imagem
    os.chdir(DirImg)
    #Pesquisa a imagem no menu principal e clica no campo
    pyautogui.click( pyautogui.locateCenterOnScreen('SelecaoEmpresa.png', confidence=0.9) ) 
    #Vai para o início da lista de empresas
    pyautogui.hotkey('ctrl','home')
    #Escreve o código da empresa
    pyautogui.typewrite(str(CodigoEmpresa))
    #Tecla enter
    pyautogui.press('enter')
    time.sleep(2)
    if TelaCertificado:
        pyautogui.press('esc')
    #Volta para o diretório atual.
    os.chdir(DirAtu)
    GeraLog(False,"Concluída a Seleção da empresa")

def SelecionaPeriodo(AnoCriacaoScript,Mes,Ano,MensagemPendencia):
    """
    Criação: 27/09/2022 Última Revisão 27/09/2022 Último Autor: Kleber
    AnoCriacaoScript = O ano que o script que está desenvolvendo foi criado. Exemplo: 2022
    Mes = Qual o mês que deseja selecionar. Exemplo: 8
    Ano = Qual o ano que deseja selecionar. Exemplo: 2022
    MensagemPendencia = Pode ser que após a seleção do período, apareça uma mensagem dizendo que não há pendências para 
                        os empregados. Informe True para que seja teclado ENTER na mensagem ou False caso seu ambiente
                        de teste não apresente esta mensagem.    
    """
    GeraLog(False,"Iniciado a Seleção do período")
    #Diretório atual
    DirAtu = os.getcwd()
    #Diretório onde está a imagem a ser pesquisada
    DirImg = "C:\GitHub\Auto_TGC\Automacao\Framework\img"
    #Acessa diretório da imagem
    os.chdir(DirImg)
    #Rotina para clicar no Ano a ser selecionado
    VoltaAno = ( (AnoCriacaoScript - Ano) )
    if VoltaAno == 1:
        VoltaAno = 0
    while VoltaAno > 0:
        pyautogui.click( pyautogui.locateCenterOnScreen('VoltaAno.png', confidence=0.9) )
        VoltaAno = VoltaAno - 1
    #Rotina para clicar no Mês a ser selecionado
    Meses = ["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"]
    Cont = 0
    for QualMes in Meses:
        Cont = Cont + 1
        if Cont == Mes:
            if datetime.now().month == Mes:
                pyautogui.doubleClick( pyautogui.locateCenterOnScreen(QualMes+'2.png', confidence=0.9) )
            else:
                pyautogui.doubleClick( pyautogui.locateCenterOnScreen(QualMes+'1.png', confidence=0.9) )
            break
    if MensagemPendencia:
        pyautogui.press('enter')
    #Clica no meio da tela para dar o foco
    pyautogui.click(815,291)
    #Volta para o diretório atual.
    os.chdir(DirAtu)
    GeraLog(False,"Concluído a Seleção do período")

def GeraLog(apagarDadosLog, TextoDoLog):
    """
    Criação: 27/09/2022 Última Revisão 27/09/2022 Último Autor: Kleber
    apagarDadosLog = Quando passado True, vai apagar o LOG. Deve ser passado informado assim, na primeira linha do plano de execução.
                     Passo False, ele mantem o conteúdo.
    TextoDoLog = Informe o texto que deseja ser demonstrado no LOG. Exemplo: "O valor do salário família está errado"
    """
    #Criação do LOG
    if (not os.path.exists("C:\\GitHub\\Auto_TGC\\Automacao\\Framework\\LogAuto.txt")) or (apagarDadosLog==True): # se o arquivo não existir, ele cria um novo. Ou para limpar os arquivos. 
        f = open("C:\\GitHub\\Auto_TGC\\Automacao\\Framework\\LogAuto.txt", "w")
        f.write("Inicio do Log\n\n") 
    #Efetuando configurações iniciais sobre o arquivo de LOG
    logging.basicConfig(filename='C:\\GitHub\\Auto_TGC\\Automacao\\Framework\\LogAuto.txt', 
                        filemode='a',
                        level=logging.DEBUG) # configuração inicial
 
    now = datetime.now() #pega a data atual           
    logging.warning(now.strftime("%d/%m/%Y, %H:%M:%S" + " - " + TextoDoLog)) # escreve no log

def PreparaAmbiente(Redmine,IniciaIntegrador,ModuloSis):
    """
    Criação: 27/09/2022 Última Revisão 27/09/2022 Último Autor: Kleber
    Redmine = Informe o número da tarefa Redmine a ser automatizada. Esta informação é a pasta onde está o banco e demais arquivos que serão utilizados. Exemplo: '108855'
    IniciaIntegrador = Informe True se para esta automação será necessário iniciar o Tron Integrador. Caso contrário, informe False
    ModuloSis = Informe qual módulo receberá a automação. Exemplo: '\Folha.exe'
    """
    #Carregando o arquivo de log
    GeraLog(False,"Iniciando a preparação do ambiente para testar a tarefa " + Redmine)

    #Verificando se o módulo está aberto, para poder fechá-lo
    ModuloEstaRodando = False
    for p in psutil.process_iter(attrs=['pid', 'name']):
        if p.info['name'] == (ModuloSis[1:] + ".exe"):
           ModuloEstaRodando = True
           break
    if  ModuloEstaRodando:
        os.system('taskkill /IM ' + ModuloSis[1:] + '.exe /F')        
        time.sleep(3)        

    #Colhendo dados sobre o serviço do Firebird para testes
    service = psutil.win_service_get('FirebirdServerTGCTRON')
    service = service.as_dict()

    #Pedindo para parar o serviço
    if (service and service['status'] == 'running'):
        os.system('net stop FirebirdServerTGCTRON')

    #Colhendo dados atualizados sobre o serviço do Firebird para testes
    service = psutil.win_service_get('FirebirdServerTGCTRON')
    service = service.as_dict()

    #Verificando, caso o serviço ainda esteja rodando, tenho que parar a execução da função
    if (service and service['status'] == 'running'):
        GeraLog(False,"ERRO - Não foi possível parar o serviço do Firebird")
        return False

    #Colhendo dados sobre o serviço do Tron Integrador para testes
    service = psutil.win_service_get('TronIntegradorSvc')
    service = service.as_dict()

    #Pedindo para parar o serviço
    if (service and service['status'] == 'running'):
        os.system('net stop TronIntegradorSvc')

    #Colhendo dados atualizados sobre o serviço do Tron Integrador para testes
    service = psutil.win_service_get('TronIntegradorSvc')
    service = service.as_dict()

    #Caso o serviço ainda esteja rodando, tenho que parar a execução da função
    if (service and service['status'] == 'running'):
        GeraLog(False,"ERRO - Não foi possível parar o serviço do Tron Integrador")
        return False

    #Excluindo relatórios gerados pelo sistema
    if os.path.exists("C:\\Users\\Public\\Documents\\Report.pdf"):
        os.remove("C:\\Users\\Public\\Documents\\Report.pdf")

    #Verificando se o arquivo foi de fato excluido. Caso contrário, tenho que parar a execução da função
    if os.path.exists("C:\\Users\\Public\\Documents\\Report.pdf"):
        GeraLog(False,"ERRO - Não foi possível excluir o arquivo Report.pdf")
        return False

    #Excluindo relatórios gerados pelo sistema
    if os.path.exists("C:\\Users\\Public\\Documents\\Report.prn"):
        os.remove("C:\\Users\\Public\\Documents\\Report.prn")

    #Verificando se o arquivo foi de fato excluido. Caso contrário, tenho que parar a execução da função
    if os.path.exists("C:\\Users\\Public\\Documents\\Report.prn"):
        GeraLog(False,"ERRO - Não foi possível excluir o arquivo Report.prn")
        return False

    #Excluindo arquivos XML utilizados anteriormente
    fileList = glob.glob('C:/Bancos/*.xml')
    for filePath in fileList:
        os.remove(filePath)

    #Verificando se os arquivos foram de fato excluidos. Caso contrário, tenho que parar a execução da função
    TemXML = False
    fileList = glob.glob('C:/Bancos/*.xml')
    for filePath in fileList:
        TemXML = True
    if TemXML:
        GeraLog(False,"ERRO - Não foi possível excluir todos os XML utilizados anteriormente")
        return False

    #Excluindo arquivos TXT utilizados anteriormente
    fileList = glob.glob('C:/Bancos/*.txt')
    for filePath in fileList:
        os.remove(filePath)

    #Verificando se os arquivos foram de fato excluidos. Caso contrário, tenho que parar a execução da função
    TemTXT = False
    fileList = glob.glob('C:/Bancos/*.txt')
    for filePath in fileList:
        TemTXT = True
    if TemTXT:
        GeraLog(False,"ERRO - Não foi possível excluir todos os TXT utilizados anteriormente")
        return False

    #Excluindo o banco utilizando anteriormente
    if os.path.exists("C:\\Bancos\\troncg.idb"):
        os.remove("C:\\Bancos\\troncg.idb")

    #Verificando se o arquivo foi de fato excluido. Caso contrário, tenho que parar a execução da função
    if os.path.exists("C:\\Bancos\\troncg.idb"):
        GeraLog(False,"ERRO - Não foi possível excluir o TRONCG.IDB")
        return False

    #Verificando se existe o arquivo de banco compactado. Caso contrário, tenho que parar a execução da função
    if not os.path.exists("C:\\Bancos\\" + Redmine + "\\Banco.rar"):
        GeraLog(False,"ERRO - Não existe o arquivo BANCO.RAR")
        return False

    #Extrai o arquivo compactado na pasta bancos
    if os.path.exists("C:\\Bancos\\" + Redmine + "\\Banco.rar"):
        patoolib.extract_archive("C:\\Bancos\\" + Redmine + "\\Banco.rar", outdir="C:\\Bancos")

    #Verificando se existe o arquivo de banco descompactado. Caso contrário, tenho que parar a execução da função
    if not os.path.exists("C:\\Bancos\\troncg.idb"):
        GeraLog(False,"ERRO - Não o arquivo TRONCG.IDB após a descompactação")
        return False

    #Extrai arquivos de importação
    if os.path.exists("C:\\Bancos\\" + Redmine + "\\Arquivos.rar"):
        patoolib.extract_archive("C:\\Bancos\\" + Redmine + "\\Arquivos.rar", outdir="C:\\Bancos")

    #Excluindo o Atualiza.bin
    if os.path.exists("C:\\Program Files (x86)\\Tron\Atualiza.bin"):
        os.remove("C:\\Program Files (x86)\\Tron\Atualiza.bin")

    #Excluindo o Atualiza.ban
    if os.path.exists("C:\\Program Files (x86)\\Tron\Atualiza.ban"):
        os.remove("C:\\Program Files (x86)\\Tron\Atualiza.ban")

    #Renomeando de OLD para BAN
    fileList = glob.glob('C:/Program Files (x86)/Tron/*.old')
    for filePath in fileList:
        os.rename(filePath,"C:/Program Files (x86)/Tron/Atualiza.ban")

    #Renomeando de REL para BIN
    fileList = glob.glob('C:/Program Files (x86)/Tron/*.rel')
    for filePath in fileList:
        os.rename(filePath,"C:/Program Files (x86)/Tron/Atualiza.bin")

    #Verificando se existe o Atualiza.bin. Caso contrário, tenho que parar a execução da função
    if not os.path.exists("C:\\Program Files (x86)\\Tron\Atualiza.bin"):
        GeraLog(False,"ERRO - Ocorreu falha ao renomear o Atualiza.bin")
        return False

    #Verificando se existe o Atualiza.ban. Caso contrário, tenho que parar a execução da função
    if not os.path.exists("C:\\Program Files (x86)\\Tron\Atualiza.ban"):
        GeraLog(False,"ERRO - Ocorreu falha ao renomear o Atualiza.ban")        
        return False

    #Iniciando o Firebird
    os.system('net start FirebirdServerTGCTRON')

    #Colhendo dados sobre o serviço do Firebird para testes
    service = psutil.win_service_get('FirebirdServerTGCTRON')
    service = service.as_dict()

    #Verificando se o serviço do Firebird foi iniciado. Caso contrário, tenho que parar a execução da função
    if not (service and service['status'] == 'running'):
        GeraLog(False,"ERRO - Ocorreu falha ao tentar iniciar o Firebird")
        return False

    #Chamando o módulo TGC
    os.startfile("C:\Program Files (x86)\Tron" + ModuloSis + ModuloSis + ".exe")

    #Aguardando a abertura do módulo
    time.sleep(10)

    #Verificando se o módulo está aberto. Caso contrário, tenho que parar a execução da função
    ModuloEstaRodando = False
    for p in psutil.process_iter(attrs=['pid', 'name']):
        if p.info['name'] == (ModuloSis[1:] + ".exe"):
            ModuloEstaRodando = True
            break
    if not ModuloEstaRodando:
        GeraLog(False,"ERRO - O processo do módulo " + ModuloSis[1:] + ".exe não está em execução")
        return False

    #Restruturando o banco. O tempo limite de espera será de 10 minutos
    #Caso tenha arquivo XML na pasta TRON, deu LOG de banco
    TempoLimite = 0
    DeuLog = False
    while os.path.exists("C:\\Program Files (x86)\\Tron\Atualiza.ban"):
        time.sleep(1)
        TempoLimite = TempoLimite + 1
        if TempoLimite > 600 or DeuLog:
            break          
        fileList = glob.glob('C:/Program Files (x86)/tron/*.xml')
        for filePath in fileList:
            DeuLog = True
            break
    if TempoLimite > 600:
        GeraLog(False,"ERRO - A estruturação do banco levou mais de 10 minutos.")
        return False

    if DeuLog:
        GeraLog(False,"ATENCAO - Ocorreu LOG de banco após a restruturação. Acionar DBA.")
    
    #Encerrando o módulo
    os.system('taskkill /IM ' + ModuloSis[1:] + '.exe /F')

    #Aguardando o processo ser fechado definitivamente
    time.sleep(3)

    #Verificando se o módulo está aberto. Caso contrário, tenho que parar a execução da função
    ModuloEstaRodando = False
    for p in psutil.process_iter(attrs=['pid', 'name']):
        if p.info['name'] == (ModuloSis[1:] + ".exe"):
            ModuloEstaRodando = True
            break
    if  ModuloEstaRodando:
        GeraLog(False,"ERRO - O processo " + ModuloSis[1:] + ".exe ainda está rodando")
        return False

    #Iniciando o processo do Tron Integrador
    if IniciaIntegrador:

        #Chamando o Tron Integrador
        os.startfile("C:\Program Files (x86)\Tron\TronIntegrador\Tron.Integrador.exe")

        #Aguardando a abertura do Integrador
        time.sleep(2)

        #Pressionando Enter na mensagem apresentada
        pyautogui.press('enter')

        #Abrindo o menu configurações
        pyautogui.hotkey('alt','c')

        #Ativando o integrador, precionando a sequencia de teclas abaixo.
        pyautogui.press(['a','s','enter','s','esc'])

        #Iniciando o Tron Integrador
        os.system('net start TronIntegradorSvc')

        #Colhendo dados sobre o serviço do Firebird para testes
        service = psutil.win_service_get('TronIntegradorSvc')
        service = service.as_dict()

        #Verificando, caso o serviço não esteja rodando, tenho que parar a execução da função
        if not (service and service['status'] == 'running'):
            GeraLog(False,"ERRO - Ocorreu falha ao iniciar o Tron Integrador")
            return False

    GeraLog(False,"Preparação do Ambiente finalizada")

    #Chamando o módulo TGC
    os.startfile("C:\Program Files (x86)\Tron" + ModuloSis + ModuloSis + ".exe")
    time.sleep(10)
    return True