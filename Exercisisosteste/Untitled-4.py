rooms = ["A120", "Annex I", "Annex II", "INE auditorium"]
starts = [20080048, 20261213, 20261394, 20261481]
ends = [20261212, 20261393, 20261480, 20262195]
counts = [0, 0, 0, 0]

student_nunber = input("Write ur nunbers : ") #20100001, 20261300,20261450, 1, 20100002
student_nunber= student_nunber.replace(" ","").split(",")
for j in range(len(student_nunber)):
    for p in range(4): 
        if int(starts[p]) <= int(student_nunber[j]) <= int(ends[p]):
            counts[p] = int(counts[p])+ 1

for i in range(len(rooms)):
    print( rooms[i] +": " + counts[i] + " students")

    