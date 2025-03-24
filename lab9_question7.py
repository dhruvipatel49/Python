def ispalindrome(string1):
    string2=string1[::-1]
    if(string1==string2):
        print("THe given string is palindrome.")
    else:
        print("The given string is not palindrome.")
str=input("Enter the string:")
check_palindrome=ispalindrome(str)
print(check_palindrome)