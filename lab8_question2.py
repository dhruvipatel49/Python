import random
random_nums={random.randint(15,45) for _ in range(10)}
print("Random number set:",random_nums)
count_lessThan_30=sum(1 for num in random_nums if num<30)
random_nums={num for num in random_nums if num<=35}
print("Count of numbers less than 30:",count_lessThan_30)
print("Set of numbers less than 35:",random_nums)