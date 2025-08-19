nome = (input("qual é o seu nome?: "))
idade =(input("qual é sua idade?: "))
if nome and idade != '':
	print('tem espaço', nome.count(""))
	print(f'seu nome é {nome}')
	print(f'sua idade é {idade}')
	print(nome[::-1])
	print('seu nome tem:', len(nome))
	print('a primeira letra do seu nome é:',nome[0])
	print('a ultima letra do seu nome é:',nome[-1])
else:
	print('digite oque se pede.')