A = int(input("Enter the value of a: "))
B = int(input("Enter the value of b: "))
C = int(input("Enter the value of c: "))
if (A+B>C and A+C>B and B+C>A):
    print("Yes its a triangle validity. ")
else:
    print("No its not a triangle validity")