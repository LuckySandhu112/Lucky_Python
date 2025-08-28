Num1 = int(input("Enter the first number: "))
Num2 = int(input("Enter the second number: "))

print("For addition press: 1" "\nFor subtraction press: 2" "\nFor multiplication press: 3" "\nFor division press: 4")
print("Calculator: ")

char = int(input("What you want to do: "))

if(char == 1):
    print(Num1, "+" ,Num2, "=" ,(Num1+Num2))
elif(char == 2):
    print(Num1, "-" ,Num2, "=" ,(Num1-Num2))
elif(char == 3):
    print(Num1, "*" ,Num2, "=" ,(Num1*Num2))
elif(char == 4):
    print(Num1, "/" ,Num2, "=" ,(Num1/Num2))
else:
    print("Not valid. ")