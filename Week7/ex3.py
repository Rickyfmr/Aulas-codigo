n_names = int(input("Quantos nomes tens no teu no me completo: "))
list_final = []
for i in range(n_names):
    nome = input("Digite o teu nome em ordem: ")
    list_final.append(nome)
print("nice to me you",list_final[0],list_final[-1])