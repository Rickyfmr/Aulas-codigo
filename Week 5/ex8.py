name = input("Enter your name: ")
if name[-1] == "a":
    name = name[:-1] + "inha"
    print(name)
elif name[-1] == "o":
    name = name[:-1] + "inho"
    print(name)