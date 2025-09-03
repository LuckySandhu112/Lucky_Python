temp = int(input("Enter the temperature in celsius: "))
print("Enter what you want to do: ")
choice = input("Enter the choice: ").upper()

match choice:
    case 'F':
        print("Temperature in Fahrenheit", (temp * 9/5) + 32 ,"°F")
    case 'K':
        print("Temperature in Kelvin", (temp + 273.15) ,"K")