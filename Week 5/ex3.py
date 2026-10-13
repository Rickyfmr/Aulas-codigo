name = input("Enter your name: ")
answer = input("whether milk should be added before the cereal? (yes/no): ")

if answer.lower() == "yes":
    print("Dear " + name + ", you cannot pass Computation I, good luck with your life.")
elif answer.lower() == "no":
    print("Dear " + name + ", congrats, you have chance to pass this class!")
else :
    print("you did not write a boolian value")