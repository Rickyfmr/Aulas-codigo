line = "Beth Smith;Morty Smith;Rick Sanchez-Smith;Morty Smith"
taken = ["rsanchez", "ssmith"]

# <A> Separar a string original por pessoa
for p in line: 

    # <B> Passar para minúsculas, remover hífens e separar nome de apelido
    parts = line.lower().lstrip("-").split(";")
    
    # <C> Criar o username (primeira letra do nome + até 5 letras do apelido)
    username = parts[0]+parts[1] 
    print
    # <D> Verificar se o username já existe na lista
    if username in taken: 
        username = username + "2"
        
    # <E> Adicionar o username final à lista 'taken'
    taken.append(username)

print(taken)
