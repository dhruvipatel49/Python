#check whether the points are collinear or not.
a,b=input("Enter first two points:").split()
c,d=input("Enter second two points:").split()
x,y=input("Enter third two points:").split()
area=(int(a)*(int(d)-int(y))+int(c)*(int(y)-int(b))+int(x)*(int(b)-int(d)))/2
if(area==0):
    print("all the points are collinear.")
else:
    print("all the points are not collinear.")
