num = int(input("Enter a number: "))
rev = 0
count = len(str(num))

for i in range(count):
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reverse of the number is:", rev)