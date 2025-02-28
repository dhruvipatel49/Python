def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = int(input("Enter n: "))
r = int(input("Enter r: "))

nCr = factorial(n) // (factorial(r) * factorial(n - r))
nPr = factorial(n) // factorial(n - r)

print("nCr:", nCr)
print("nPr:", nPr)