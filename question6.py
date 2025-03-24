def function(x):
    list=[(i,i**2,i**3) for i in range(1,x+1)]
    print(list)
x=int(input("Enter the number:"))
result=function(x)
print(result)
