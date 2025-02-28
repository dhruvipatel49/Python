list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list3 = [num for num in list1 if num not in list2]
print("First list:", list1)
print("Second list:", list2)
print("Resulting list:", list3)