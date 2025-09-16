cursos = []

 
opcao_cursos = {
	
	1: "Engenharia I",
	2: "Java I",
	3: "React JS I",
    4: "Banco de dados I"

}

opcao_horario = {
	1: "18:00 - 19:00",
	2: "19:00 - 20:00",
	3: "20:30 - 21:30",
	4: "21:30 - 22:30"

}

def mostrar_opcoes(dicionario, titulo):
    print(f"\n{titulo}")
    for chave, valor in dicionario.items():
        print(f"{chave} - {valor}")
        
        
def escolha(dicionario, tipo):
	try:	
		return int(input(f"Escolha {tipo}"))
		if escolha in dicionario:
			return escolha
		else:
			print("Opção inválida ")
			return None
	except ValueError:
		print("entrada inválida")
		return None
		


mostrar_opcoes(opcao_cursos,"Cursos")
escolha(opcao_cursos,"cursos")

mostrar_opcoes(opcao_horario,"Cursos")
escolha(opcao_horario,"cursos")