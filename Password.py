password = input("Enter your password: ")

if len(password) < 8:
    print("Password is too short! It must be at least 8 characters.")
else:
    print(password ,"Password length is acceptable.")