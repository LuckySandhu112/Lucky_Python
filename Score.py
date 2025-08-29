Score = int(input("Enter the score: "))

if(Score >= 90):
    print("Your grade is: A")
elif(Score >=75 and Score < 90):
    print("Your grade is: B")
elif(Score >= 50 and Score < 75):
    print("Your grade is: C")
elif(Score < 50):
    print("You are fail. ")
else:
    print("Invalid....")