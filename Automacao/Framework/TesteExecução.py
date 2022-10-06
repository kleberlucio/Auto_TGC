from repository_comuns import *
from repository_escrita import *
import sys

#pyautogui.click(1803,16)

try:
    if not PreparaAmbiente('108805',False,'\Escrita'):
        sys.exit(1)
    if not SelecionaEmpresa(13,False):
        sys.exit(1)
    SelecionaPeriodo(2022,4,2017,False)
    if not VerificaEmpresaPeriodoSelecionado('13','4','2017'):
        sys.exit(1)
    if not QuebraApuracaoEscrita('04','2017'):
        sys.exit(1)
    if not ApuraICMS_IPI_EFD(3,15,False):
        sys.exit(1)
    if not GeraSpedFiscal(12):
        sys.exit(1)
    if not ComparaArquivo("C:/Tron/SPED Fiscal - EFD/00013/IPANEMA GRAFICA E EDITORA LTDA 042017 Livro.txt",
                          "C:/GitHub/Auto_TGC/Automacao/Escrita_Fiscal/Geracao_De_Informacoes_Oficiais/SPED_Fiscal/108805/IPANEMA GRAFICA E EDITORA LTDA 042017 Livro.txt",
                          "C:\\GitHub\\Auto_TGC\\Automacao\\Escrita_Fiscal\\Geracao_De_Informacoes_Oficiais\\SPED_Fiscal\\108805\\Difer.txt"):
        sys.exit(1)
except:
    GeraLog(False,"Interrompido os testes sobre o cenário 108805, verificar LOG acima")

