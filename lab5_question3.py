import random

numbers = [random.randint(1, 30) for _ in range(50)]
unique_numbers = list(set(numbers))

print("Original list:", numbers)
print("List without duplicates:", unique_numbers)