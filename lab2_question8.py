#check whether the triangle is valid or not.
a=int(input("Enter the first angle:"))
b=int(input("Enter the second angle:"))
c=int(input("Enter the third angle:"))

total=a+b+c
if(total==180):
    print("It is a valid triangle.")
else:
    print("It is not a valid triangle.")