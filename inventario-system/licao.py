produtos = []
qnts = int(input("Quantos itens? "))
controle = 0

for item in range(0, qnts):
    produtos.append(str(input(f"item: {item + 1} ")))


busca = str(input("Qual item quer buscar: "))
for elemento in produtos:
    if elemento == busca:
        controle = 1
        

if controle == 0:
    print(f"O item {busca} nao esta na lista.")

else:
    print(f"O item {busca} esta na lista.")


