entrada = input('E - entrar S - sair')
senha = input('senha: ')

senha_certa = "123"
if (entrada == 'E' or entrada == 'e') and senha == senha_certa:
	print("bem-vindo")
else:
	print('até logo')