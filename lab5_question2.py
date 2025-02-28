import random

numbers = [random.randint(1, 100) for _ in range(20)]
target = int(input("Enter a number: "))
positions = [i for i, num in enumerate(numbers) if num == target]

print("Generated list:", numbers)
print("Positions of occurrences:", positions)