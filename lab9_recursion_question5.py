def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)

a = int(input("Enter base (a): "))
b = int(input("Enter exponent (b): "))
print("Result:", power(a, b))