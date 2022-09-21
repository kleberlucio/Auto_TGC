from datetime import datetime
import time

def GeraLog(IniciaLog, TextoDoLog):
    now = datetime.now()
    if IniciaLog:
        f = open("c:\Bancos\LogAuto.txt","w+")
    f=open("c:\Bancos\LogAuto.txt", "a+")
    f.write(now.strftime("%m/%d/%Y, %H:%M:%S") + " - " + TextoDoLog + '\n')
    f.close()

now = datetime.now()
GeraLog(True,"iniciando o log")
GeraLog(False,"Ocorreu falha ao renomear o Atualiza.bin")
time.sleep(5)
GeraLog(False,"Ocorreu falha ao renomear o Atualiza.ban")