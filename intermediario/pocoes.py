'''
Remur chegou na loja de poções de um amigo que ele conhecia a mais de 200 anos.
o amigo lhe deu boas vindas!
Remur o comprimentou e olhou para a prateleira..ele observou mais de perto e já sabia qual iria pegar, poção de salgueiro para melhorar suas poções, poção amerallda para poçoes de anestésico e pocao ametista para criacao de poções que curavam urticária.
Remur - hoje vou levar a poção salgueiro, amerallda e ametista.
Elgar - quer levar outra ?
Remur - só isso por hoje meu amigo, me passe o valor.
Elgar disse o valor.
Remur - Deve esta tão caro assim por causa da amerallda ... 
Elgar - é amerallda é sempre mais caro, e os anoes sempre aumentam o preco.
'''

bolsa = []

pocoes = {
	1: {"nome":"Amerallda","preco":50.20},
	22: {"nome":"Salgueiro","preco":20.30},
	34: {"nome":"Ametista", "preco":30.40}
}


#pedido = int(input("Oque vai ser hoje amigo ?"))

def mostra_menu():
	print("Menu")
	for prateleira, item in pocoes.items():
		print(f"{prateleira} - {item['nome']} - {item['preco']}")
		
		
#escolher pocao
def escolher_pocao():
	try:
		escolha = int(input("Oque será hoje ?"))
		if escolha in pocoes:
			return menu[escolha]
		else:
			print("Opção inválida.")
			return None
	except ValueError:
			print("Entrada inválida. Digite o número da prateleira.")
			return None

mostra_menu()
escolher_pocao()