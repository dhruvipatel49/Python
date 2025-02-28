#Print largest and smallest values out of three
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))
if(a>=b and a>=c):
    print("a is the largest")
    if(b>=c):
        print("c is the smallest")
    else:
        print("b is the smallest")
elif(b>=a and b>=c):
    print("b is the largest")
    if(a>=c):
        print("c is the smallest")
    else:
        print("a is the smallest")
else:
    print("c is the largest")
    if(b>=a):
        print("a is the smallest")
    else:
        print("b is the smallest")