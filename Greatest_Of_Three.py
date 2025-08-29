Num1 = int(input("Enter the first number: "))
Num2 = int(input("Enter the second number: "))
Num3 = int(input("Enter the third number: "))

if(Num1 > Num2 and Num1 > Num3):
    print(Num1, "is the greatest. ")
elif(Num1 < Num2 and Num3 < Num2):
    print(Num2, "is the greatest. ")
elif(Num3 > Num1 and Num3 > Num2):
    print(Num3, "is the greatest. ")
elif(Num1 == Num2 and Num1 == Num3 and Num2 == Num3):
    print("All three numbers are same")
else:
    print("Invalid....")