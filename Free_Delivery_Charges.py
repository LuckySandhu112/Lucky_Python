Amount = int(input("Enter the ordered amount: "))

if(Amount >= 500):
    print("You get a free delivery, Order amount is: ", Amount)
else:
    print("Your order amount is: ", (Amount + 50))