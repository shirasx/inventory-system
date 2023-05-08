from inventario_fun import *
from time import sleep
while True:
    escolha = 0
    escolha = menu(escolha)

    if escolha == 1:
        adicionar(produtos)
    elif escolha == 2:
        nome_busca = input("Digite o nome do produto: ").title()
        arquivo_csv = "save.csv"
        found = buscar(nome_busca, arquivo_csv)
        if found:
            print("Produto encontrado:")
            for chave, valor in found.items():
                print(f"{chave}: {valor}")
            sleep(2)
        else:
            print("Produto não encontrado.")
            sleep(2)
    elif escolha == 3:
        mostraDados()
    elif escolha == 4:
        nome_apaga = input("Nome do item para apagar: ")
        apagaItem(nome_apaga)
    elif escolha == 5:
        print("Saindo...")
        break
    else:
        print("Opção invalida.")



