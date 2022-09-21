from datetime import datetime
import os
import psutil
import patoolib
import glob
import time
import pyautogui

def GeraLog(IniciaLog, TextoDoLog):
    now = datetime.now()
    if IniciaLog:
        f = open("c:\Bancos\LogAuto.txt","w+")
    f=open("c:\Bancos\LogAuto.txt", "a+")
    f.write(now.strftime("%d/%m/%Y, %H:%M:%S") + " - " + TextoDoLog + '\n')
    f.close()

def PreparaAmbiente(Redmine,IniciaIntegrador,ModuloSis):

    #Carregando o arquivo de log
    GeraLog(True,"Iniciando a preparação do ambiente para testar a tarefa " + Redmine)

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
        GeraLog(False,"Não foi possível parar o serviço do Firebird")
        return        

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
        GeraLog(False,"Não foi possível parar o serviço do Tron Integrador")
        return

    #Excluindo relatórios gerados pelo sistema
    if os.path.exists("C:\\Users\\Public\\Documents\\Report.pdf"):
        os.remove("C:\\Users\\Public\\Documents\\Report.pdf")

    #Verificando se o arquivo foi de fato excluido. Caso contrário, tenho que parar a execução da função
    if os.path.exists("C:\\Users\\Public\\Documents\\Report.pdf"):
        GeraLog(False,"Não foi possível excluir o arquivo Report.pdf")
        return

    #Excluindo relatórios gerados pelo sistema
    if os.path.exists("C:\\Users\\Public\\Documents\\Report.prn"):
        os.remove("C:\\Users\\Public\\Documents\\Report.prn")

    #Verificando se o arquivo foi de fato excluido. Caso contrário, tenho que parar a execução da função
    if os.path.exists("C:\\Users\\Public\\Documents\\Report.prn"):
        GeraLog(False,"Não foi possível excluir o arquivo Report.prn")
        return

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
        GeraLog(False,"Não foi possível excluir todos os XML utilizados anteriormente")
        return

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
        GeraLog(False,"Não foi possível excluir todos os TXT utilizados anteriormente")
        return

    #Excluindo o banco utilizando anteriormente
    if os.path.exists("C:\\Bancos\\troncg.idb"):
        os.remove("C:\\Bancos\\troncg.idb")

    #Verificando se o arquivo foi de fato excluido. Caso contrário, tenho que parar a execução da função
    if os.path.exists("C:\\Bancos\\troncg.idb"):
        GeraLog(False,"Não foi possível excluir o TRONCG.IDB")
        return

    #Verificando se existe o arquivo de banco compactado. Caso contrário, tenho que parar a execução da função
    if not os.path.exists("C:\\Bancos\\" + Redmine + "\\Banco.rar"):
        GeraLog(False,"Não existe o arquivo BANCO.RAR")
        return

    #Extrai o arquivo compactado na pasta bancos
    if os.path.exists("C:\\Bancos\\" + Redmine + "\\Banco.rar"):
        patoolib.extract_archive("C:\\Bancos\\" + Redmine + "\\Banco.rar", outdir="C:\\Bancos")

    #Verificando se existe o arquivo de banco descompactado. Caso contrário, tenho que parar a execução da função
    if not os.path.exists("C:\\Bancos\\troncg.idb"):
        GeraLog(False,"Não o arquivo TRONCG.IDB após a descompactação")
        return

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
        GeraLog(False,"Ocorreu falha ao renomear o Atualiza.bin")
        return

    #Verificando se existe o Atualiza.ban. Caso contrário, tenho que parar a execução da função
    if not os.path.exists("C:\\Program Files (x86)\\Tron\Atualiza.ban"):
        GeraLog(False,"Ocorreu falha ao renomear o Atualiza.ban")        
        return

    #Iniciando o Firebird
    os.system('net start FirebirdServerTGCTRON')

    #Colhendo dados sobre o serviço do Firebird para testes
    service = psutil.win_service_get('FirebirdServerTGCTRON')
    service = service.as_dict()

    #Verificando se o serviço do Firebird foi iniciado. Caso contrário, tenho que parar a execução da função
    if not (service and service['status'] == 'running'):
        GeraLog(False,"Ocorreu falha ao tentar iniciar o Firebird")
        return

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
        GeraLog(False,"O processo do módulo " + ModuloSis[1:] + ".exe não está em execução")
        return

    #Restruturando o banco. O tempo limite de espera será de 10 minutos
    #Caso tenha arquivo XML na pasta TRON, deu LOG de banco
    TempoLimite = 0
    DeuLog = False
    while os.path.exists("C:\\Program Files (x86)\\Tron\Atualiza.ban"):
        time.sleep(1)
        TempoLimite = TempoLimite + 1
        if TempoLimite > 600:
            break          
        fileList = glob.glob('C:/Program Files (x86)/tron/*.xml')
        for filePath in fileList:
            DeuLog = True
            break
    if TempoLimite > 600:
        GeraLog(False,"A estruturação do banco levou mais de 10 minutos.")
        return

    if DeuLog:
        GeraLog(False,"Ocorreu LOG de banco após a restruturação. Acionar DBA.")
    
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
        GeraLog(False,"O processo " + ModuloSis[1:] + ".exe ainda está rodando")
        return

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

        #Iniciando o Firebird
        os.system('net start TronIntegradorSvc')

        #Colhendo dados sobre o serviço do Firebird para testes
        service = psutil.win_service_get('TronIntegradorSvc')
        service = service.as_dict()

        #Verificando, caso o serviço não esteja rodando, tenho que parar a execução da função
        if not (service and service['status'] == 'running'):
            GeraLog(False,"Ocorreu falha ao iniciar o Tron Integrador")
            return

    GeraLog(False,"Preparação do Ambiente finalizada")

    #Chamando o módulo TGC
    os.startfile("C:\Program Files (x86)\Tron" + ModuloSis + ModuloSis + ".exe")

    time.sleep(15)
