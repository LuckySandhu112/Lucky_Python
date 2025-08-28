Time = int(input("Enter the time: "))
print("The time is:", Time , "hrs")

if(Time <= 2):
    print("The parking charges will be: 20")
elif(Time > 2 and Time <= 5):
    print("The parking charges will be: 50")
else:
    print("The parking charges will be: 100")