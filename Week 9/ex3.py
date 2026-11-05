numeroamigos = int(input("Quantos amigos vais convidar"))
friends = input("escreve o nome dos teus amigos e separa por virgula")
friendlist = friends.rsplit(",")
count=0
for i in range(len(friendlist)):
    if friendlist[i][0] in "A" : #Relembrar que posso fazer isto!!
        count = count+1
print(count,"people's name starts with an A.")