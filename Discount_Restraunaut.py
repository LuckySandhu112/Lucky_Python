Amount = int(input("Enter the bill amount: "))

if(Amount <= 1000):
    print("The discount will be 5%" "\n The bill amount is: ", Amount * (5/100))
elif(Amount > 1000 and Amount <= 2000):
    print("The discount will be 10%"  "\n The bill amount is: ", Amount * (10/100))
elif(Amount > 2000 and Amount <= 3000):
    print("The discount will be 15%" "\n The bill amount is: ", Amount * (15/100))
else:
    print("The discount will be 25%" "\n The bill amount is: ", Amount * (25/100))