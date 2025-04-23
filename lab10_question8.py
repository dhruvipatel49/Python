f1=open(r"C:\Users\Vidhi\Desktop\source.txt",'r')
f2=open(r"C:\Users\Vidhi\Desktop\destination3.txt",'w')
r1=f1.read()
for i in r1:
    if i==' a ' or i==' an ' or i=='the':
        f2.write(' ')
    else:
        f2.write(i)
f1.close()
f2.close()