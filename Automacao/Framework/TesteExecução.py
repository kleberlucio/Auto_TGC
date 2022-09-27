from repository_functions import *

#def Redmine_108805():

#pyautogui.click(1803,16)
#time.sleep(2)

PreparaAmbiente('108805',False,'\Escrita')
#time.sleep(2)
SelecionaEmpresa(13,False)
#time.sleep(2)
SelecionaPeriodo(2022,4,2017,False)
#time.sleep(2)
QuebraApuracaoEscrita('04','2017')
#time.sleep(2)
ApuraICMS_IPI_EFD(3,15,False)
#time.sleep(2)
GeraSpedFiscal(12)
#time.sleep(2)
ComparaArquivo("C:/Tron/SPED Fiscal - EFD/00013/IPANEMA GRAFICA E EDITORA LTDA 042017 Livro.txt",
               "C:/GitHub/Auto_TGC/Automacao/Escrita_Fiscal/Geracao_De_Informacoes_Oficiais/SPED_Fiscal/108805/IPANEMA GRAFICA E EDITORA LTDA 042017 Livro.txt",
               "C:\\GitHub\\Auto_TGC\\Automacao\\Escrita_Fiscal\\Geracao_De_Informacoes_Oficiais\\SPED_Fiscal\\108805\\Difer.txt")







