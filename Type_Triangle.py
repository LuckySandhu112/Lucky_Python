a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if(a+b > c and b+c > a and a+c > b):
    if(a == b and b == c):
        print("It is an Equilateral triangle. ")
    elif(a == b or b == c or a == c):
        print("It is an Isosceles triangle. ")
    else:
        print("It is a scalene triangle. ")
else:
    print("It is not a valid triangle. ")