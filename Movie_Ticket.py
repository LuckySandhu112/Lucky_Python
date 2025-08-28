Age = int(input("Enter the age: "))

if(Age <= 18):
    print("The ticket price is: 100")
elif(Age > 18 and Age <= 30):
    print("The ticket price is: 200")
elif(Age > 30 and Age <= 40):
    print("The ticket price is: 300")
elif(Age > 40 and Age <= 50):
    print("The ticket price is: 400")
else:
    print("The ticket price is: 500")