f1=open(r"C:\Users\Vidhi\Desktop\source1.txt",'w')
f2=open(r"C:\Users\Vidhi\Desktop\source2.txt",'w')
f1.writelines('Today is thursday \nWe have 23 apples\n')
f2.writelines('12 apples were stolen \nWe are left with 11 apples\n')
f1.close()
f2.close()

f1=open(r"C:\Users\Vidhi\Desktop\source1.txt",'r')
f2=open(r"C:\Users\Vidhi\Desktop\source2.txt",'r')
f3=open(r"C:\Users\Vidhi\Desktop\destination1.txt",'w')

r1=f1.readlines()
r2=f2.readlines()

maxlen=max(len(r1),len(r2))

for i in range(maxlen):
    if i<len(r1):
        f3.write(r1[i])
    if i<len(r2):
        f3.write(r2[i])

f1.close()
f2.close()
f3.close()