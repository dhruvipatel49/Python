#accept a number from a user and print the number of digits in it.
number=int(input("Enter the number:"))
count=0
if number<0:
    number= -number
while number >0:
    number=number//10
    count+=1
print("Number of digits:",count)