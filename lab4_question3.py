string = input("Enter a string: ")
alphabets = sum(c.isalpha() for c in string)
digits = sum(c.isdigit() for c in string)
print("Alphabets:", alphabets)
print("Digits:", digits)