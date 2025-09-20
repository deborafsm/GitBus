grade = []

 
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
		
		
def main():
	while opcao_cursos and opcao_horario:
		mostrar_opcoes(opcao_cursos,"Cursos disponíveis.")
		curso_escolhido = escolha(opcao_cursos,"cursos")
		if curso_escolhido is None:
			continue

		mostrar_opcoes(opcao_horario,"Horários disponíveis.")
		horario_escolhido = escolha(opcao_horario,"horário")
		
		#add a grade e remove as opcoes da lista.

		grade.append((opcao_cursos[curso_escolhido], opcao_horario[horario_escolhido]))
		del opcao_cursos[curso_escolhido]
		del opcao_horario[horario_escolhido]
		print("Curso e horário adicionados com sucesso!")
		
		print("\nGrade final:")
		for i, (curso, horario) in enumerate(grade, 1):
			print(f"{i}. {curso} - {horario}")
			
main()