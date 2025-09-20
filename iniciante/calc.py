#calculadora.

def menu():
	
	print("1 adição")
	print("2 subtração")
	print("3 multiplicação")
	print("4 divisão")


menu()
escolha = int(input("escolha uma opção"))
n1 = float(input("Digite um número:"))
n2 = float(input("Digite outro número: "))


def calculadora():
	if escolha == 1:
		print(f"Resultado: {n1 + n2}")
	if escolha == 2:
		print(f"Resultado: {n1 - n2}")
	if escolha == 3:
		print(f"Resultado: {n1 * n2} ")
	if escolha == 4:
		print(f"Resultado: {n1 / n2}")
		
calculadora()