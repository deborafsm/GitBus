#in entre
#not in nao está entre

palavra = input("Digite uma palavra:  ")
entre = input("Digite oque deseja encontrar: ")

if entre in palavra:
	print(f'{entre} está em {palavra}')
else:
	print(f'{entre} não está entre {palavra}')