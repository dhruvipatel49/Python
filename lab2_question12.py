#check if the given point is insid ,on th or outside the circle
import math
a,b=map(int,input("Enter the coordinates of the circle:").split())
x,y=map(int,input("Enter the coordinates of the given point:").split())

distance=math.sqrt((x-a)**2+(y-b)**2)
r=int(input("Enter the radius:"))
if(distance==0):
    print("The given point is at the center.")
elif(distance<r and distance>0):
    print("The given point is inside the circle but not on the center.")
elif(distance==r):
    print("The given point is on the circle.")
else:
    print("The given point is out side the circle.")