from Folha_CalculoRescisao import *

GeraLog(False,"Iniciada a execução das automações do servidor 02")
try:
    # Folha de Pagamento
    #   Rescisão
    #       Cálculo de Rescisão Normal/Complementar
    Redmine_79489()
    GeraLog(False,"Concluída a execução das automações do servidor 02")
except:
    GeraLog(False,"Ocorreu algum erro de excessão em relação a execução das automações")