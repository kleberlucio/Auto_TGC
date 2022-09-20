import os
import time
import pyautogui
import psutil

#Chamando o Tron Integrador
os.startfile("C:\Program Files (x86)\Tron\TronIntegrador\Tron.Integrador.exe")

time.sleep(2)

#Pressionando Enter na mensagem apresentada
pyautogui.press('enter')

pyautogui.hotkey('alt','c')

pyautogui.press(['a','s','enter','s','esc'])

#Iniciando o Firebird
os.system('net start TronIntegradorSvc')

#Colhendo dados sobre o serviço do Firebird para testes
service = psutil.win_service_get('TronIntegradorSvc')
service = service.as_dict()