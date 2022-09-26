import sys

#sys.path.append( '\\GitHub\\Auto_TGC\\Automação\\Framework' )
sys.path.insert(0, '/GitHub/Auto_TGC/Automacao/Framework')
 
from repository_functions import *


PreparaAmbiente('123456',False,'\GerCont')
SelecionaEmpresa('23')
SelecionaPeriodo(2022,5,2019)

