num = int(input("Enter a number: "))

# Check prime
prime = num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))

# Check perfect
perfect = sum(i for i in range(1, num) if num % i == 0) == num

# Check Armstrong
armstrong = sum(int(d)**len(str(num)) for d in str(num)) == num

# Check palindrome
palindrome = str(num) == str(num)[::-1]

# Check automorphic
automorphic = str(num**2).endswith(str(num))

print("Prime:", prime)
print("Perfect:", perfect)
print("Armstrong:", armstrong)
print("Palindrome:", palindrome)
print("Automorphic:", automorphic)