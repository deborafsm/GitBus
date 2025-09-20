velocidade = 70
local_carro = 100

RADAR = 60
LOCAL = 100
RADAR_RANGE = 1

vel_carro_pass_radar = velocidade > RADAR
carro_passou_radar = local_carro >= (LOCAL - RADAR_RANGE) and local_carro <= (LOCAL + RADAR_RANGE)
carro_multado_radar = carro_passou_radar and vel_carro_pass_radar

if velocidade > RADAR:
	print('Velocidade carro passou do radar 1')

if carro_multado_radar and vel_carro_pass_radar:
	print('carro multado em radar')