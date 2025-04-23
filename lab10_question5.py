f1=open(r"C:\Users\Vidhi\Desktop\source.txt",'w')
f1.writelines('Today is thursday \nWe have 23 apples \n12 apples were stolen \nWe are left with 11 apples')
f1.close()

f1=open(r"C:\Users\Vidhi\Desktop\source.txt",'r')
f2=open(r"C:\Users\Vidhi\Desktop\destination.txt",'w')
r=f1.read()
for i in r:
    if i.islower:
        f2.write(i.upper())
    else:
        f2.write(i)
        
f1.close()
f2.close()