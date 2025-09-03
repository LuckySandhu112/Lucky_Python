num1 = int(input("Enter the first number: "))
num2 = int((input("Enter the second number: ")))
Operator = input(("Enter the operator: "))

match Operator:
    case '+':
        print("The sum is: ", num1 + num2)
    case '-':
        print("The sum is: ", num1 - num2)
    case '*':
        print("The multiplication is: ", num1 * num2)
    case '/':
        if(num2 != 0):
            print("The division is: ",num1 / num2)
        else:
            print("Can't divide by zero. ")
    case _:
        print("...Invalid operator...")