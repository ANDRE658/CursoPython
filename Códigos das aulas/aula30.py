'''
CONSTANTE = "Váriaveis" que não vão mudar
Muitas cindições no mesmos if (ruim)
    <- Contagem de complexidade (ruim)

'''
velocidade = 61 #Velocidade atual do carro
local_carro = 100 # local em que o carro está na estrada 

RADAR_1 = 60 # velocidade maxima do radar
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGER = 1 # A distancia onde o radar pega

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro <= (LOCAL_1 + RADAR_RANGER) and local_carro >= (LOCAL_1 - RADAR_RANGER)
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

if velocidade > RADAR_1:
    print(f'Você utrapassou a velocidade permitida!')

if carro_multado_radar_1:
    print(f'Carro multado em radar 1')