def sum_and_count(lst, index=0):
    if index == len(lst):
        return (0, 0)
    total, count = sum_and_count(lst, index + 1)
    return (lst[index] + total, 1 + count)

def average(lst):
    total, count = sum_and_count(lst)
    return total / count if count != 0 else 0

numbers = [4, 8, 15, 16, 23, 42]
print("Average:", average(numbers))