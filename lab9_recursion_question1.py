def prime_factors(n, i=2):
    if i > n // 2:
        if n > 1:
            print(n, end=' ')
        return
    if n % i == 0:
        print(i, end=' ')
        prime_factors(n // i, i)
    else:
        prime_factors(n, i + 1)

num = int(input("Enter a positive integer: "))
if num > 0:
    prime_factors(num)
else:
    print("Invalid input")