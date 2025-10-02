lista_livros =[]
estante = {
	1:{"nome":"A fera","preco":50.89,"categoria":"fantasia épica"},
	2:{"nome":"O corvo cinza","preco":70.89,"categoria":"fantasia épica"},
	3:{"nome":"A fenix","preco":50.99,"categoria":"fantasia épica"},
}

def mostra_livros():
	for livro, item in estante.items():
		print(f"{estante}")
	
	
mostra_livros()