#Print largest and smallest values out of two
num1,num2=input().split()
if(num1>num2):
    print("First number",num1,"is the largest and second number",num2,"is the smallest one")
elif(num2>num1):
    print("Second number",num2,"is the largest and first number",num1,"is the smallest one")
else:
    print("Both are equal.")