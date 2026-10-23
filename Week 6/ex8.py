def exam_sit(attended,count,held):
     if (float (attended + count)/ held)  >= 0.60:
         return True
     return False


held = int(input("HELD "))
attended = int(input("attended "))
count = 0
for i in range (1, (held - attended) + 1): # todas as que faltou
    resposta = input("have a medical cause for absences (Y or N). ")
    if resposta == "Y" :
        count = count + 1
    elif resposta == "N" :
        print("not justified")


if exam_sit(attended, count, held) == True:
    print("Percentage is 60.0% with medical cause, you CAN attend the exam.")
    
else:
    print("Percentage is 60.0%, you CANNOT attend the exam.")
