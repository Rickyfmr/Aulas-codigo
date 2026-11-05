nunbers = []
while len(nunbers) <= 4:
    nunber = input("escreve um dos numeros que vão para a lista de 5 numeros inteiros: ")
    nunbers.append(nunber)
for i in range(len(nunbers)):
   if int(nunbers[i]) > 10:
       print(nunbers[i],"is bigger than 10 and at index", i)