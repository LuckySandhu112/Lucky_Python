char = input("Enter the alphabet: ").lower()

if char in('a', 'e', 'i', 'o', 'u'):
    print("It is a vowel. ", char)
else:
    print("It is a consonant. ", char)