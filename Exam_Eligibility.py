Attendance = int(input("Enter your Attendance percentage: "))
Marks = int(input("Enter your marks: "))

if(Attendance >= 75):
    if(Marks >= 40):
        print("Yes you are eligible. ")
    else:
        print("Not eligible")
else:
    print("Your percentage is low.")