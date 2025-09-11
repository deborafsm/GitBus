#var de escopo geraal
emocao_lista = []
def emotions():

	print("Entre com a sua emocao de hoje")
	print("1 Feliz 😄")
	print("2 Triste 😢")
	print("3 Neutro 😐")
	print("4 Chateado(a) 😡")


emotions()
emocao = int(input("digite a sua emocao de hoje"))

def add_lista():
	if emocao == 1:
		emocao_lista.append("Feliz 😄")
	elif emocao == 2:
		emocao_lista.append("Triste 😢 ")
	elif emocao == 3:
		emocao_lista.append("Neutro 😐 ")
	elif emocao == 4:
		emocao_lista.append("Chateado(a) 😡")
	else:
		print("opção inválida.")
	
		
			
					
add_lista()
print(emocao_lista)
	