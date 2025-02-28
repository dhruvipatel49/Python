a,b,c=map(int,input("Enter the marks of three subjects:").split())
total=a+b+c
average=total/3
print("the total marks are",total,"and average marks are",average)
if(average>39):
    print("passed")
else:
    print("failed")
if(80<=a<=100):
    print("O grade")
elif(70<=a<=79):
    print("A+ grade")
elif(60<=a<=69):
    print("A grade")
elif(50<=a<=59):
    print("B+ grade")
elif(45<=a<=49):
    print("C grade")
elif(40<=a<=44):
    print("P grade")
elif(0<=a<=39):
    print("F grade")
else:
    print("absent")   

if(80<=b<=100):
    print("O grade")
elif(70<=b<=79):
    print("A+ grade")
elif(60<=b<=69):
    print("A grade")
elif(50<=b<=59):
    print("B+ grade")
elif(45<=b<=49):
    print("C grade")
elif(40<=b<=44):
    print("P grade")
elif(0<=b<=39):
    print("F grade")
else:
    print("absent")

if(80<=c<=100):
    print("O grade")
elif(70<=c<=79):
    print("A+ grade")
elif(60<=c<=69):
    print("A grade")
elif(50<=c<=59):
    print("B+ grade")
elif(45<=c<=49):
    print("C grade")
elif(40<=c<=44):
    print("P grade")
elif(0<=c<=39):
    print("F grade")
else:
    print("absent")