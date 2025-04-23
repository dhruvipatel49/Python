import csv
d = {}
with open(r"E:\college\Python\lab10Q1.csv", 'r', newline='') as f:
    r = csv.reader(f)
    header = next(r)
    for i in r:
        rollno = i[0]
        name = i[1] 
        CP = int(i[2])
        Chemistry = int(i[3])
        professional_communication = int(i[4])
        t=CP+Chemistry+professional_communication
        d[rollno] = [name, CP, Chemistry, professional_communication,t] 
print(d)

with open(r"E:\college\Python\lab10Q1.csv", 'r', newline='') as f:
    r = csv.DictReader(f)
    header = next(r)
    for i in r:
        print(i)