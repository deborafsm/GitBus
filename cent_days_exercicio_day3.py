valor_total = 0

altura = input(("você tem 1.20 de altura ?"))

if "sim":
	print("pode subir")
else:
	print("não pode subir")
	
idade = input("qual é a sua idade ?")

if int(idade) < 12:
	valor_total += 5
	print("O ingresso 🎫 custa R$5,00")
if int(idade) > 12 and int(idade) < 18:
	valor_total += 7
	print("o ingresso 🎫 custará R$7,00")
else:
	valor_total += 12
	print("O ingresso 🎫 custará R$12.00")
	
photo = input("você quer tirar fotos ? sim ou não ")

if "sim":
	valor_total += 10
	print(f"para tirar foto é {valor_total}")
else:
	print(f"{preco}")