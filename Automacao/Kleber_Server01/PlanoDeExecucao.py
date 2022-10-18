from Geracao_SPED_Fiscal import *

GeraLog(False,"Iniciada a execução das automações do servidor 01")
try:
    #Escrita Fiscal
    #   Geracao_De_Informacoes_Oficiais
    #       SPED_Fiscal
    Redmine_108805()
    GeraLog(False,"Concluída a execução das automações do servidor 01")
except:
    GeraLog(False,"Ocorreu algum erro de excessão em relação a execução das automações")