def sum_average(n1,n2,n3,n4,n5):
    result={"total":0,"average":0}
    result["total"]=n1+n2+n3+n4+n5
    result["average"]=result["total"]/5
    return result
a,b,c,d,e=map(int,input("Enter the numbers:").split())
result=sum_average(a,b,c,d,e)
print("The total of five numbers and average of the numbers are",result)