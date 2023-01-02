def main():

    x = int(input("X = "))
    y = int(input("Y = "))

    operation = input(("Which operation do you want to perform? (+, -, *, /)"))

    if operation == "+":
        sum = add(x,y)
        print(sum)
    elif operation == "-":
        substraction = substract(x,y)
        print(substraction)
    elif operation == "*":
        multiplication = multiply(x,y)
        print(multiplication)
    elif operation == "/":
        division = divide(x,y)
        print(division)
    else:
        print("That's not something I can help you with!")

def add(a,b):
    return a + b
def substract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b

main()