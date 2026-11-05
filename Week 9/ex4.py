names = ["Anthony", "Gertrude", "Gertrudo", "Anthonella"]
count = 0
for i in range(len(names)):
    for j in range(len(names[i])):
        if names[i][j].lower() in "aeiou":
            print("found one!")
            count= count+1

print(count) #funciona pq aparece 12