# Lista para armazenar emoções

emocao_lista = []

# Dicionário de opções /opcoes de emocoes

opcoes_emocao = {

    1: "Feliz 😄",

    2: "Triste 😢",

    3: "Neutro 😐",

    4: "Chateado(a) 😡",
    
    0: "para sair.."

}
#funcao para chamar o menu
def mostrar_menu():
#pergunta para o usuario como ele está se sentindo aquele dia.
    print("\nComo você está se sentindo hoje?")
#percorre pela lista de emocoes existentes.
#chave = 1,2, 3...
#valor = Feliz 😄 , Triste 😢 ...
#em lista que se chama opcoes_emocao...
    for chave, valor in opcoes_emocao.items():
#aqui ele so mostra oque ele percorreu no for..
        print(f"{chave} - {valor}")


#outra funcao para obter a emocao..
def obterEmocao():
#ele comeca tentando...pegar um digito entre 1- 4 	
	try:
		return int(input("Digite um número que corresponda a sua emoção: "))
	except ValueError:
		return -1
		
#outra funcao para logica d tratamento das opcoes..
def main():
	#enquanto for verdade ou diferente de 0.
	while True:
		#para comecar ele mostra o menu.
		mostrar_menu()
		#variavel escolha é a funcao que pega o valor.
		escolha = obterEmocao()
		
	#se for 0 é a opcao sair ...entao rle para e mostra as emocoes.	
		if escolha == 0:
			print ("obrigada por compartilhar suas emoções.")
			break
		
#enquanto for a opcao 1 a 4 ser colocada ele add numa lista, la em cima tem uma lista vazia que se chama emocao_lista.
		if escolha in opcoes_emocao:
			emocao_lista.append((opcoes_emocao[escolha]))
	
#se vc colocar uma opcao 5 > ele vai printar que a escolha é invalida e vai retornar la no comeco while tru.	
		else:
			print("opção inválida.")
	
#agr se vc colocar 0 vc vai sair do looping e dai o sist vai te mostrar q lista das emocoes que vc registrou 	
	print("Emoções registradas")
	for i, emocao in enumerate(emocao_lista,1):
		print(f"{i} {emocao}")
		
				
#aqui chama a funcao main							
main()
			