from operator import truediv
import os
import psutil
import time
import glob



#Chamando o MenuTron
os.startfile("C:\Program Files (x86)\Tron\Folha\Folha.exe")

time.sleep(10)

FolhaEstaRodando = False

#PONTO DE PARADA. Conferindo se a folha abriu. 
for p in psutil.process_iter(attrs=['pid', 'name']):
    if p.info['name'] == "Folha.exe":
        FolhaEstaRodando = True
        break

if not FolhaEstaRodando:
    print("A Folha não está em execução")

TempoLimite = 0
DeuLog = False
while os.path.exists("C:\\Program Files (x86)\\Tron\Atualiza.ban"):
    time.sleep(1)
    TempoLimite = TempoLimite + 1
    if TempoLimite > 600:
        # PONTO DE PARADA, estourou mais de 10 minutos para estruturar ou ocorreu erro
        print("Gastou mais de 10 minuto para estruturar o banco")
        break
    #Verificando se tem XML na pasta TRON. Se tiver, deu LOG na restruturação
    fileList = glob.glob('C:/Program Files (x86)/tron/*.xml')
    for filePath in fileList:
        DeuLog = True
        break


FolhaEstaRodando = False





for p in psutil.process_iter(attrs=['pid', 'name']):
    if p.info['name'] == "Folha.exe":
        FolhaEstaRodando = True

if FolhaEstaRodando:
    print('A Folha não foi encerrada')