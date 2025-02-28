fahrenheit = [32, 50, 77, 104, 212]
celsius = [(temp - 32) * 5 / 9 for temp in fahrenheit]
print("Fahrenheit list:", fahrenheit)
print("Celsius list:", celsius)