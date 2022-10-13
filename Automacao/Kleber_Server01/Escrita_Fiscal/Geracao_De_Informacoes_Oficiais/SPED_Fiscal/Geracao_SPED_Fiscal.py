

import sys
import os
#sys.path.insert(0,'C:\GitHub\Auto_TGC\Automacao\Framework')

#C:\GitHub\Auto_TGC\Automacao\Kleber_Server01\Escrita_Fiscal\Geracao_De_Informacoes_Oficiais\SPED_Fiscal

#C:\GitHub\Auto_TGC\Automacao\Framework

from repository_comuns import *
from repository_escrita import *

def Redmine_108805():
    try:
        if not repository_comuns.PreparaAmbiente('108805', False, '\Escrita'):
            sys.exit(1)
        if not repository_comuns.SelecionaEmpresa(13,False):
            sys.exit(1)
        repository_comuns.SelecionaPeriodo(2022,4,2017,False)
        if not repository_comuns.VerificaEmpresaPeriodoSelecionado('13','4','2017'):
            sys.exit(1)
        if not repository_escrita.QuebraApuracaoEscrita('04','2017'):
            sys.exit(1)
        if not repository_escrita.ApuraICMS_IPI_EFD(3,15,False):
            sys.exit(1)
        if not repository_escrita.GeraSpedFiscal(12):
            sys.exit(1)
        if not repository_comuns.ComparaArquivo("C:\\Tron\\SPED Fiscal - EFD\\00013\\IPANEMA GRAFICA E EDITORA LTDA 042017 Livro.txt",
                            "C:\\GitHub\\Auto_TGC\\Automacao\\Escrita_Fiscal\\Geracao_De_Informacoes_Oficiais\\SPED_Fiscal\\Arquivos\\IPANEMA GRAFICA E EDITORA LTDA 042017 Livro.txt",
                            "C:\\GitHub\\Auto_TGC\\Automacao\\Escrita_Fiscal\\Geracao_De_Informacoes_Oficiais\\SPED_Fiscal\\Difer_108805.txt"):
            sys.exit(1)
    except:
        repository_comuns.GeraLog(False, "Interrompido os testes sobre o cenário 108805, verificar LOG acima")
    return True