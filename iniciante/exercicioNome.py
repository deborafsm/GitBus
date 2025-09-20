nome = input("Digite seu nome: ")
tamanho = len(nome)
if tamanho >= 1:
	if tamanho <= 4:
		print("nome curto")
	if tamanho >= 5 and tamanho <= 6:
		print("seu nome é normal")
	else:
		print("nome grande")
	
	
	
	
else:
	print("digite pelo menos uma letra.")