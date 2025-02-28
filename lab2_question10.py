#compare the area and perimeter of a rectangle.
l=int(input("Enter the length:"))
b=int(input("Enter the width:"))
area=l*b
perimeter=2*(l+b)
if(area>perimeter):
    print("Area is greater than the perimeter")
elif(area<perimeter):
    print("Area is less than the perimeter")
else:
    print("Both are equal.")
    