#O Apotecário Maluco tem um cardápio de poções mágicas, cada uma com um preço diferente.
#Ele quer um programa que ajude os clientes a escolherem suas poções e calcular o preço total.
#Crie um dicionário com o nome das poções como chaves e os preços como valores.
menu = {
    "Poção de Cura": 50,    
    "Poção de Força": 75,
    "Poção de Invisibilidade": 100,
    "Poção de Velocidade": 60,
    "Poção de Sabedoria": 80
}
def mostra_menu():
    print("Menu de Poções:")
    for nome, preco in menu.items():
        print(f"{nome}: {preco} moedas de ouro")

mostra_menu()

