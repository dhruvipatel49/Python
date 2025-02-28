string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

found = False
for i in range(len(string1) - len(string2) + 1):
    if string1[i:i+len(string2)] == string2:
        found = True
        break

if found:
    print("Second string is present in the first string.")
else:
    print("Second string is not present in the first string.")