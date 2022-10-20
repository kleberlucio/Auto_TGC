from repository_comuns import *
from repository_folha import *
import sys

def Redmine_105():
    try:
        GeraLog(False, "Iniciando os teste da Folha - Redmine_105")
        
        PreparaAmbiente('108805', False, '\Folha')
        SelecionaEmpresa(13, True, 'Folha')        
        SelecionaPeriodo(2022, 10, 2022, False, True)      
        VerificaEmpresaPeriodoSelecionado('13','10','2022')
        InserirRescisao(3, 5, 171)
        
        PressionarTeclas(['enter','enter','enter'])       
        EscreverTexto('05102022')
        PressionarTeclas('enter')
        EscreverTexto('05102022')
        PressionarTeclas('enter')
        EscreverTexto('1')
        PressionarTeclas('enter')
        EsperarTempo(8)
        
        if not ExisteImagem('C:\\GitHub\\Auto_TGC\\Automacao\\Kleber_Server01\\Folha_Pagamento\\Rescisao\\Calculo_Rescisao\\img\\Redmine_101010_calculo_rescisao.png', 5):
            GeraLog(False, "ERRO - Cálculo da rescisão errado")
            return False
    except:
        GeraLog(False, "Interrompido os testes sobre o cenário 100000, verificar LOG acima")
        sys.exit(1)
    GeraLog(False,"Terminado os teste da Folha")
    return True

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Redmine_105()
