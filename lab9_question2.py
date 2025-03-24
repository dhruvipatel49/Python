def compute(n):
   result={"count": 0}
   result["count"]=n+n*n+n*n*n+n*n*n*n
   return result

num=int(input("Enter the num:"))
count=compute(num)
print(count)