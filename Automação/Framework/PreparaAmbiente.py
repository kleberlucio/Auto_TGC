import os
import psutil
import patoolib
import glob
import time

def PreparaAmbiente(Redmine):

    #Colhendo dados sobre o serviço do Firebird para testes
    service = psutil.win_service_get('FirebirdServerTGCTRON')
    service = service.as_dict()

    #Pedindo para parar o serviço
    if (service and service['status'] == 'running'):
        os.system('net stop FirebirdServerTGCTRON')

    #Colhendo dados atualizados sobre o serviço do Firebird para testes
    service = psutil.win_service_get('FirebirdServerTGCTRON')
    service = service.as_dict()

    #PONTO DE PARADA. Caso o serviço ainda esteja rodando, tenho que parar a execução da função
    if (service and service['status'] == 'running'):
        return
        #Criar LOG de erro aqui

    #Colhendo dados sobre o serviço do Tron Integrador para testes
    service = psutil.win_service_get('TronIntegradorSvc')
    service = service.as_dict()

    #Pedindo para parar o serviço
    if (service and service['status'] == 'running'):
        os.system('net stop TronIntegradorSvc')

    #Colhendo dados atualizados sobre o serviço do Tron Integrador para testes
    service = psutil.win_service_get('TronIntegradorSvc')
    service = service.as_dict()

    #PONTO DE PARADA. Caso o serviço ainda esteja rodando, tenho que parar a execução da função
    if (service and service['status'] == 'running'):
        return
        #Criar LOG de erro aqui

    #Excluindo relatórios gerados pelo sistema
    if os.path.exists("C:\\Users\\Public\\Documents\\Report.pdf"):
        os.remove("C:\\Users\\Public\\Documents\\Report.pdf")

    #Verificando se o arquivo foi de fato excluido. Caso contrário, tenho que parar a execução da função
    if os.path.exists("C:\\Users\\Public\\Documents\\Report.pdf"):
        return
        #Criar LOG de erro aqui

    #Excluindo relatórios gerados pelo sistema
    if os.path.exists("C:\\Users\\Public\\Documents\\Report.prn"):
        os.remove("C:\\Users\\Public\\Documents\\Report.prn")

    #Verificando se o arquivo foi de fato excluido. Caso contrário, tenho que parar a execução da função
    if os.path.exists("C:\\Users\\Public\\Documents\\Report.prn"):
        return
        #Criar LOG de erro aqui

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
        return
        #Criar LOG de erro aqui

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
        return
        #Criar LOG de erro aqui

    #Excluindo o banco utilizando anteriormente
    if os.path.exists("C:\\Bancos\\troncg.idb"):
        os.remove("C:\\Bancos\\troncg.idb")

    #Verificando se o arquivo foi de fato excluido. Caso contrário, tenho que parar a execução da função
    if os.path.exists("C:\\Bancos\\troncg.idb"):
        return
        #Criar LOG de erro aqui

    #Verificando se existe o arquivo de banco compactado. Caso contrário, tenho que parar a execução da função
    if not os.path.exists("C:\\Bancos\\" + Redmine + "\\Banco.rar"):
        return
        #Criar LOG de erro aqui

    #Extrai o arquivo compactado na pasta bancos
    if os.path.exists("C:\\Bancos\\" + Redmine + "\\Banco.rar"):
        patoolib.extract_archive("C:\\Bancos\\" + Redmine + "\\Banco.rar", outdir="C:\\Bancos")

    #Verificando se existe o arquivo de banco descompactado. Caso contrário, tenho que parar a execução da função
    if not os.path.exists("C:\\Bancos\\troncg.idb"):
        return
        #Criar LOG de erro aqui

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
        return
        #Criar LOG de erro aqui

    #Verificando se existe o Atualiza.ban. Caso contrário, tenho que parar a execução da função
    if not os.path.exists("C:\\Program Files (x86)\\Tron\Atualiza.ban"):
        return
        #Criar LOG de erro aqui

    #Iniciando o Firebird
    os.system('net start FirebirdServerTGCTRON')

    #Colhendo dados sobre o serviço do Firebird para testes
    service = psutil.win_service_get('FirebirdServerTGCTRON')
    service = service.as_dict()

    #Verificando se o serviço do Firebird foi iniciado. Caso contrário, tenho que parar a execução da função
    if not (service and service['status'] == 'running'):
        return
        #Criar LOG de erro aqui

    #Chamando o módulo de Folha de Pagamento
    os.startfile("C:\Program Files (x86)\Tron\Folha\Folha.exe")

    #Aguardando a abertura do módulo
    time.sleep(10)

    #Verificando se o módulo está aberto. Caso contrário, tenho que parar a execução da função
    FolhaEstaRodando = False
    for p in psutil.process_iter(attrs=['pid', 'name']):
        if p.info['name'] == "Folha.exe":
            FolhaEstaRodando = True
            break
    if not FolhaEstaRodando:
        print("A Folha não está em execução")

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
        return
        #Criar LOG de erro aqui
    if DeuLog:
        return
        #Criar LOG de erro aqui