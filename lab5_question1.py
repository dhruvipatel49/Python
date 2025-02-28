import random

odds = [random.randint(1, 99) | 1 for _ in range(5)]
evens = [random.randint(1, 99) & ~1 for _ in range(4)]

odds[2] = evens

flattened = sorted([item for sublist in odds for item in (sublist if isinstance(sublist, list) else [sublist])])

print("List of 5 odd integers:", odds)
print("List of 4 even integers:", evens)
print("Flattened and sorted list:", flattened)