#var de escopo geraal
emocao_lista = []
def emotions():

	print("Entre com a sua emocao de hoje")
	print("1 Feliz 😄")
	print("2 Triste 😢")
	print("3 Mais ou menos 🫤")
	print("4 Raiva 😡")


emotions()
emocao = int(input("digite a sua emocao de hoje"))

if emocao == 1:
	emocao_lista.append("Feliz 😄")
	
print(emocao_lista)
