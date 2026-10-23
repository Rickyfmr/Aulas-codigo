user_word = input("escreve a tua palavra com a s: ")
user_letter = input("escreve a tua letra : ")
count = 0
for i in range(len(user_word)):
    if user_word[i] == user_letter :
        count = count + 1
print (count)