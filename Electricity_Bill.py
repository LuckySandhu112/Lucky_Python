Bill = int(input("Enter the unit: "))

if(Bill <= 100):
    print("The bill is: ", Bill*5)
elif(Bill > 100 and Bill <=300):
    print("The bill is: ", Bill*10)
elif(Bill > 300 and Bill <= 500):
    print("The bill is: ", Bill*15)
else:
    print("The bill is: ", Bill*20)