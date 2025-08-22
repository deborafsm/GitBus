#try except 
numero = input('digite um numero: (vou dobrar o valor) ')

try:
	numero_float = float(numero)
	print(numero_float *2)
except:
	print('isso nao é um numero')