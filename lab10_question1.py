import csv

# Data to write (can be customized)
data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "Los Angeles"],
    ["Charlie", 28, "Chicago"]
]

# Create and write to a CSV file
with open("people.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file 'people.csv' created successfully.")
