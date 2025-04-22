def reverse_list(lst):
    if len(lst) <= 1:
        return lst
    return [lst[-1]] + reverse_list(lst[:-1])

numbers = [1, 2, 3, 4, 5]
reversed_numbers = reverse_list(numbers)
print(reversed_numbers)