operation = int(input("Choose an operation (1 for multiplication, 2 for addition, 3 for a raised to the power of b): "))


def multiply(a, b):
    return a * b
def add(a, b):
    return a + b
def power(a, b):
    return a ** b


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if operation == 1:
    result = multiply(a, b)
    print(result)
elif operation == 2:
    result = add(a, b)
    print(result)
elif operation == 3:
    result = power(a, b)
    print(result)