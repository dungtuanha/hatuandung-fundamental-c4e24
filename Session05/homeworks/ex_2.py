prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

items = list(prices)

total = 0
for fruit in prices:
    print(fruit)
    print("price:", prices[fruit])
    print("stock:", stock[fruit])
    total = total+ (prices[fruit] * stock[fruit])
    
print("______________________________________________________________________")
print("Total:", total)