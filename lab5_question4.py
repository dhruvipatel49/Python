import random

numbers = [random.randint(-50, 50) for _ in range(30)]
positives = [num for num in numbers if num > 0]
negatives = [num for num in numbers if num < 0]

print("Original list:", numbers)
print("Positive numbers:", positives)
print("Negative numbers:", negatives)