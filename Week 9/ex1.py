l1 = [1, 2, 3, 4, 5]
l2 = [5, 8, 2, 9]
for i in range(len(l1)):
    for j in range(len(l2)):
        if l1[i] == l2[j]:
            print(l1[i])