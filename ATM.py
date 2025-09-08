Pin = "1234"
Balance = 5000
Entered_Pin = input("Enter the pin: ")
if Entered_Pin == Pin:
    amount = int(input("Enter the amount to withdraw: "))
    if amount <= Balance:
        Balance -= amount
        print("Withdraw successful! ")
        print("Remaining Balance: ", Balance)
    else:
        print("Error: Insufficient balance.")
else:
    print("Error: Incorrect PIN.")