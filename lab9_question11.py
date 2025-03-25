def createlist(list1,list2):
    set1=set(list1)
    set2=set(list2)
    set3=set1.intersection(set2)
    list3=list(set3)
    list4=sorted(list3)
    print(list4)
list1=[12,13,24,67,7,8]
list2=[67,8,98,56,13,77]
intersection=createlist(list1,list2)
print(intersection)