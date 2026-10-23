nunber_itens = int(input("Digite o número de itens que vais comparar: "))
list_final = []
for i in range(nunber_itens):
    item = input("Digite o nome do item: ")
    list_final.append(item)
print(list_final)