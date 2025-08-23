Name = input("Enter your name: ")
Marks1 = int(input("Marks obtained in Maths: "))
Marks2 = int(input("Marks obtained in English: "))
Marks3 = int(input("Marks obtained in Science: "))
avg = (Marks1 + Marks2 + Marks3)/3
percentage = (Marks1 + Marks2 + Marks3)/300 * 100

print("Name: ", Name)
print(" Maths | English | Science ")
print(" ", Marks1 , "  |  ",   Marks2, "   |   ", Marks3)
print("Average marks: ", avg)
print("Percentage: ", percentage)