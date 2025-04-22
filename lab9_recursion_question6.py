def sanitize_list(lst, index=0):
    if index == len(lst):
        return lst
    if lst[index] < 0:
        lst[index] = 0
    return sanitize_list(lst, index + 1)

numbers = [3, -1, 5, -7, 9, -2]
sanitize_list(numbers)
print(numbers)