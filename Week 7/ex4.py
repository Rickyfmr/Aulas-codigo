my_lista = input("Define a list with four positive integers of your choosing separa com ,: ").replace(" ","").split(",")
my_lista[0] = 100
somardaslistas = 0 
for i in range(len(my_lista)):
    if int(my_lista[i]) >= 6 :
        somardaslistas = somardaslistas + int(my_lista[i])
print(somardaslistas)