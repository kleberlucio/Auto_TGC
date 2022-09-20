import os
import psutil
import patoolib
import glob

#Colhendo dados sobre o serviço do Firebird para testes
service = psutil.win_service_get('FirebirdServerTGCTRON')
service = service.as_dict()

#Pedindo para parar o serviço
if (service and service['status'] == 'running'):
    os.system('net stop FirebirdServerTGCTRON')

#Colhendo novos dados sobre o serviço do Firebird para testes
service = psutil.win_service_get('FirebirdServerTGCTRON')
service = service.as_dict()

#PONTO DE PARADA. Caso o serviço ainda esteja rodando, tenho que parar a execução das automações
if (service and service['status'] == 'running'):
    print('O serviço do Firebird não parou com sucesso')

#Colhendo dados sobre o serviço do Tron Integrador para testes
service = psutil.win_service_get('TronIntegradorSvc')
service = service.as_dict()

#Pedindo para parar o serviço
if (service and service['status'] == 'running'):
    os.system('net stop TronIntegradorSvc')

#Colhendo novos dados sobre o serviço do Tron Integrador para testes
service = psutil.win_service_get('TronIntegradorSvc')
service = service.as_dict()

#PONTO DE PARADA. Caso o serviço ainda esteja rodando, tenho que parar a execução das automações
if (service and service['status'] == 'running'):
    print('O serviço do Tron Integrador não parou com sucesso')

#Excluindo relatórios gerados pelo sistema
if os.path.exists("C:\\Users\\Public\\Documents\\Report.pdf"):
    os.remove("C:\\Users\\Public\\Documents\\Report.pdf")

#Excluindo relatórios gerados pelo sistema
if os.path.exists("C:\\Users\\Public\\Documents\\Report.prn"):
    os.remove("C:\\Users\\Public\\Documents\\Report.prn")

#Excluindo arquivos XML utilizados anteriormente
fileList = glob.glob('C:/Bancos/*.xml')
for filePath in fileList:
    os.remove(filePath)

#Excluindo arquivos TXT utilizados anteriormente
fileList = glob.glob('C:/Bancos/*.txt')
for filePath in fileList:
    os.remove(filePath)

#Excluindo o banco utilizando anteriormente
if os.path.exists("C:\\Bancos\\troncg.idb"):
    os.remove("C:\\Bancos\\troncg.idb")

#PONTO DE PARADA. Teste para parar as automações caso o banco não tenha sido excluído
if os.path.exists("C:\\Bancos\\troncg.idb"):
    print('Ocorreu falha ao tentar apagar o arquivo Troncg.idb')

#Extrai o arquivo compactado na pasta bancos
if os.path.exists("C:\\Bancos\\123456\\Banco.rar"):
    patoolib.extract_archive("C:\\Bancos\\123456\\Banco.rar", outdir="C:\\Bancos")

#PONTO DE PARADA. Teste para parar as automações caso o banco não tenha sido extraído
if not os.path.exists("C:\\Bancos\\troncg.idb"):
    print('Ocorreu falha ao extrair o arquivo Troncg.idb')

#Extrai arquivos de importação
if os.path.exists("C:\\Bancos\\123456\\Arquivos.rar"):
    patoolib.extract_archive("C:\\Bancos\\123456\\Arquivos.rar", outdir="C:\\Bancos")

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

#Iniciando o Firebird
os.system('net start FirebirdServerTGCTRON')

#Colhendo dados sobre o serviço do Firebird para testes
service = psutil.win_service_get('FirebirdServerTGCTRON')
service = service.as_dict()

#PONTO DE PARADA. Caso não tenha iniciado, parar automações
if not (service and service['status'] == 'running'):
    print('Não foi iniciado o Firebird')

#Chamando o MenuTron
os.system('"C://Program Files (x86)//Tron//menutron.exe"')

#PONTO DE PARADA. Conferindo se o MenuTron abriu. 
for p in psutil.process_iter(attrs=['pid', 'name']):
    if not ("menutron.exe" in (p.info['name']).lower()):
        print('O Menu Tron não está aberto')
