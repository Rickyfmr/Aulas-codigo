# Write here what's wrong with the code.
# Then, correct it below.

guests = "Jim,Pam,Dwight"
names = guests.split(",")
names.append("Michael")

long = 0
for name in names:
    print(f"Welcome, {name.upper()}!")
    if len(str(name)) > 3:
        long = long + 1
if "Pam" in guests:
    print("Pam is in! " + "Last to arrive: "+ names[-1])
print(f"{long} guests have long names.")

