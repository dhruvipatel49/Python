def to_binary(n):
    if n > 1:
        to_binary(n // 2)
    print(n % 2, end='')

num = int(input("Enter a positive integer: "))
if num > 0:
    to_binary(num)
else:
    print("Invalid input")