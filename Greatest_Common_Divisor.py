def gcd(a,b):
    while b!= 0:
        a,b=b,a%b
    return a
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

print("gcd of",num1,"and",num2,"is:" , gcd(num1,num2))