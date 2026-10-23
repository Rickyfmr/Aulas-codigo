my_lista = input("Define a list with four positive integers of your choosing separa com ,: ").replace(" ","").split(",")
count_odd = 0
count_even = 0
for i in range(len(my_lista)):
    print(my_lista)
    if (int(my_lista[i]) % 2) == 0:
        count_even = count_even + 1
    else :    
        count_odd = count_odd + 1

print("there are ", count_even ,"even nunbers")
print("there are ", count_odd ,"odd nunbers")