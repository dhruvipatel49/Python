grocery_prices = {"apple": 2.5, "banana": 1.2, "milk": 3.0, "bread": 2.0, "eggs": 5.0}
grocery_quantity = {"apple": 4, "banana": 6, "milk": 2, "bread": 1, "eggs": 1}

total_bill = sum(grocery_prices[item] * grocery_quantity[item] for item in grocery_prices if item in grocery_quantity)
print("Total Bill:", total_bill)