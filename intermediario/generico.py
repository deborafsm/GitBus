# ✅ Etapa 1: Criar o Menu

menu = {
    1: {"nome": "X-Burger", "preco": 27.90},
    2: {"nome": "X-Salada", "preco": 27.90},
    3: {"nome": "X-Egg", "preco": 31.90},
    4: {"nome": "X-Cheff", "preco": 46.90},
    5: {"nome": "X-Veg", "preco": 42.90}
}

def mostrar_menu():
    print("\n--- MENU ---")
    for numero, item in menu.items():
        print(f"{numero} - {item['nome']} R${item['preco']:.2f}")
        
#✅ Etapa 2: Função para Escolher Item
def escolher_item():
    try:
        escolha = int(input("\nDigite o número do lanche desejado: "))
        if escolha in menu:
            return menu[escolha]
        else:
            print("Opção inválida.")
            return None
    except ValueError:
        print("Entrada inválida. Digite um número.")
        return None

#✅ Etapa 3: Adicionar Item ao Pedido
pedido = []

def adicionar_ao_pedido(item):
    pedido.append(item)
    print(f"\n✅ {item['nome']} adicionado ao pedido.")

    print("\n🧾 Pedido atual:")
    for i, item in enumerate(pedido, 1):
        print(f"{i}. {item['nome']} - R${item['preco']:.2f}")
#✅ Etapa 4: Calcular Valor Total

def calcular_total():
    total = sum(item['preco'] for item in pedido)
    print(f"\n💰 Valor total: R${total:.2f}")

#✅ Etapa 5: Organizar com main()

def main():
    print("🍔 Bem-vindo à Lanchonete da Débora!")

    while True:
        mostrar_menu()
        item = escolher_item()
        if item:
            adicionar_ao_pedido(item)
            calcular_total()

        continuar = input("\nDeseja adicionar mais itens? (s/n): ").lower()
        if continuar != 's':
            break

    mostrar_resumo()
#🧠 Desafio Extra: Resumo Final + Remoção de Item
def mostrar_resumo():
    print("\n📦 Resumo do Pedido:")
    for i, item in enumerate(pedido, 1):
        print(f"{i}. {item['nome']} - R${item['preco']:.2f}")
    calcular_total()

    remover = input("\nDeseja remover algum item? (s/n): ").lower()
    if remover == 's':
        try:
            indice = int(input("Digite o número do item a remover: "))
            if 1 <= indice <= len(pedido):
                removido = pedido.pop(indice - 1)
                print(f"❌ {removido['nome']} removido do pedido.")
                mostrar_resumo()
            else:
                print("Número inválido.")
        except ValueError:
            print("Entrada inválida.")
#roda tudo

if __name__ == "__main__":
    main()
