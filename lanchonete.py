#mostrar menu 
#pegar o pedido do cliente.
# moatrar o valor

pedido = []

menu = {
	1: "X-Burger R$27,90",
	2: "X-Salada R$27,90",
	3: "X-Egg R$31,90",
	4: "X-Cheff R$46,90",
	5: "X-Veg R$42,90"
}

def mostra_menu():
	for numero, descricao in menu.items():
		print(f"{numero} - {descricao}")



mostra_menu()