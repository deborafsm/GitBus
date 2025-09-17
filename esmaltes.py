#cor de esmalte de cada semana.


#lista das cores e cada semana
semana_cores =[]

cores ={
	1: "Roxo",
	2: "Preto",
	3: "Azul",
	4: "Prata",
	5: "Verde"
}

semana ={

	1:"1ª semana",
	2:"2ª semana",
	3:"3ª semana",
	4:"4ª semana",
	5:"5ª semana"
}

#mostrar os esmaltes e os dias da semana 
def mostrar_listas(dicionario, titulo):
	print(f"\n,{titulo}")
	for chave, valor in dicionario.items():
		print(f"{chave} - {valor}")


#pega a escolha do usuario
def escolha(dicionario, tipo):
	try:
		return int(input(f"Escolha {tipo}"))
		if escolha in dicionario:
			return escolha
		else:
			print("Opção inválida")
			return None
	except ValueError:
		print("Entrada inválida")
		return None


def main():
	while esmalte and semana:
		mostrar_listas(cores, "Esmaltes")
		escolhe_esmalte = escolha(esmalte, "esmalte")
		if escolhe_esmalte is None:
			continue
		mostrar_listas(horario, "Semana")
		escolhe_semana = escolha(semana, "Semanan")
			




mostrar_listas(semana, "Semana")
		
