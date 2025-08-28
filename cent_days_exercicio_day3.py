altura = input(("você tem 1.20 de altura ?"))

if "sim":
	print("pode subir")
else:
	print("não pode subir")
	
idade = input("qual é a sua idade ?")

if int(idade) < 12:
	print("O ingresso 🎫 custa R$5,00")
if int(idade) > 12 and int(idade) < 18:
	print("o ingresso 🎫 custará R$7,00")
else:
	print("O ingresso 🎫 custará R$12.00")