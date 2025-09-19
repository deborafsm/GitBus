# lista das cores e cada semana
semana_cores = []

cores = {
    1: "Roxo",
    2: "Preto",
    3: "Azul",
    4: "Prata",
    5: "Verde"
}

semana = {
    1: "1ª semana",
    2: "2ª semana",
    3: "3ª semana",
    4: "4ª semana",
    5: "5ª semana"
}

# mostrar os esmaltes e os dias da semana 
def mostrar_listas(dicionario, titulo):
    print(f"\n{titulo}")
    for chave, valor in dicionario.items():
        print(f"{chave} - {valor}")

# pega a escolha do usuário
def escolha(dicionario, tipo):
    try:
        opcao = int(input(f"Escolha {tipo}: "))
        if opcao in dicionario:
            return opcao
        else:
            print("Opção inválida")
            return None
    except ValueError:
        print("Entrada inválida")
        return None

def main():
    while cores and semana:  # repete enquanto existirem opções
        mostrar_listas(cores, "Esmaltes")
        escolhe_esmalte = escolha(cores, "esmalte")
        if escolhe_esmalte is None:
            continue  # volta pro começo se escolha inválida

        mostrar_listas(semana, "Semana")
        escolhe_semana = escolha(semana, "semana")
        if escolhe_semana is None:
            continue

        semana_cores.append((cores[escolhe_esmalte], semana[escolhe_semana]))

        del cores[escolhe_esmalte]   # remove cor usada
        del semana[escolhe_semana]   # remove semana usada

        print("Adicionado com sucesso!")
        print("\nEscolha de esmalte para cada semana:")
        for i, (e, s) in enumerate(semana_cores, 1):
            print(f"{i}. {e} - {s}")

main()