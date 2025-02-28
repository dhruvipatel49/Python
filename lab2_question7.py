#find whether the year is a leap year or not.
year=int(input("Enter the year:"))
if(year%4==0):
    print(year,"year is a leap year")
else:
    print(year,"year is not a leap year")