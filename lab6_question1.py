names = [("John",), "Alice", ("Mike",), "Emma", ("David",), "Sophia"]
boys_count = sum(1 for name in names if isinstance(name, tuple))
girls_count = len(names) - boys_count
print("Boys:", boys_count, "Girls:", girls_count)