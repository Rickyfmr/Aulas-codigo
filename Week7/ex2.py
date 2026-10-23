my_list = input("escreve uma list e separa com uma , os valores: ").replace(" ","").split(",")
my_list_new=[]
for i in range(len(my_list)):
    if (int(my_list[i]) % 2) == 0:
        my_list_new.append(int(my_list[i])*2)
    if (int(my_list[i])%3 )== 0:
        my_list_new.append(int(my_list[i])*3)
print(my_list_new)