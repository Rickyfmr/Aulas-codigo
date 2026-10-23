user_word = input("escreve a tua palavra com a s: ")
count = 0
for i in range(len(user_word)):
    if user_word[i] !=  ( "a" , "e",  "i" , "u" ,"o" ):
        count = count + 1
print (count)