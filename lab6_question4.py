food_prices = [("Burger", 5), ("Pizza", 12), ("Pasta", 8), ("Salad", 6)]
for i in range(len(food_prices)):
    for j in range(len(food_prices) - i - 1):
        if food_prices[j][1] < food_prices[j + 1][1]:
            food_prices[j], food_prices[j + 1] = food_prices[j + 1], food_prices[j]
print(food_prices)