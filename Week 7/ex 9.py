n = int(input("how many children will you have? "))
name= []
count_vowels = 0
for i in range(n):
    child_name = input("what is the name of your child? ")
    name.append(child_name)
    if child_name[0].lower() in "aeiou":
        count_vowels = count_vowels + 1
print(count_vowels, "names begin with a vowel")
