Name1 = input("Enter first persons name: ")
Name2 = input("Enter second persons name: ")
Name3 = input("Enter third persons name: ")

Age1 = int(input("Enter " + Name1 + "'s age: "))
Age2 = int(input("Enter "+ Name2 + "'s age: "))
Age3 = int(input("Enter "+ Name3 + "'s age: "))

if(Age1 <= Age2 and Age1 <= Age3):
    print(Name1, "is the youngest.")
elif(Age2 <= Age1 and Age2 <= Age3):
    print(Name2, "is the youngest. ")
else:
    print(Name3, "is the youngest. ")