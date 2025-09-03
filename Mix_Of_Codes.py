while True:
    print("\n______MENU_______")
    print("1. Even Odd")
    print("2. Print Day name")
    print("3. Simple Calculator")
    print("4. Exit...")
    
    choice = input("Enter the number: ")

    match choice:
        case 1:
            num = int(input("Enter the number: "))
            
            if(num %2 == 0):
                print("It is an even number.")
            else:
                print("It is an odd number.")

        case 2:
            day = int(input("Enter the number: "))
            match day:
                case 1:
                    print("The day is Monday")
                case 2:
                    print("The day is Tuesday")
                case 3:
                    print("The day is Wednesday")
                case 4:
                    print("The day is Thursday")
                case 5:
                    print("The day is Friday")
                case 6:
                    print("The day is Saturday")
                case 7:
                    print("The day is Sunday")

        case 3:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            Operator = input("Choose the operator: ")

            match Operator:
                case '+':
                    print("The sum is: ", num1 + num2)
                case '-':
                    print("The subtraction is: ", num1 - num2)
                case '*':
                    print("The multiplication is: ", num1 * num2)
                case '/':
                    if(num2 != 0):
                        print("Can't be divided by zero.")
                    else:
                        print("The division is: ", num1/num2)

        case 4:
            print("____Exit____")

        case _:
            print("Invalid Operator")