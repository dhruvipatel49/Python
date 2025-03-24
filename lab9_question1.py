def lower_upper(s):
   result={"uppercase": 0,"lowercase": 0}
   for char in s:
      if char.isupper():
         result["uppercase"]+=1
      elif char.islower():
         result["lowercase"]+=1
   return result
string=input("Enter the string:")
count=lower_upper(string)
print(count)