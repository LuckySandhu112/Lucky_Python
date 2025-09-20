Num = int(input("Enter the number: "))
a = Num//100
b = (Num//10)%10
c = Num % 10

if(a**3 + b**3 + c**3 == Num):
    print("It is an Armstrong number. ")
else:
    print("Not an Armstrong number. ")