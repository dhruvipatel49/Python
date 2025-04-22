def string_length(s):
    if s == '':
        return 0
    return 1 + string_length(s[1:])

text = input("Enter a string: ")
print("Length:", string_length(text))