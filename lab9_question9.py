def is_alpha_digit(string):
    alphabets = sum(c.isalpha() for c in string)
    digits = sum(c.isdigit() for c in string)
    print("Alphabets:",alphabets," Digits:",digits)
str=input("Enter the string:")
print("Count of alphabets and digits in a given string is:")
count=is_alpha_digit(str)
