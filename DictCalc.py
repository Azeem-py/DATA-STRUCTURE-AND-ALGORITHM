prices = {
 'ACME': 45.23,
 'AAPL': 612.78,
 'IBM': 205.55,
 'HPQ': 37.20,
 'FB': 10.75
}

# min_price = min(zip(prices.values(), prices.keys()))
# max_price = max(zip(prices.values(), prices.keys()))
# sorted_prices = sorted(zip(prices.values(), prices.keys()))

# print('minimum price: ', min_price)
# print('maximum price: ', max_price)
# print('sorted prices: ', sorted_prices)

# min_price = min(zip(prices.keys(), prices.values(),))
# print(min_price)


# when using zip(), take note that it creates an iterator that can only be used once. Take the code below as an example
# prices_and_names = zip(prices.values(), prices.keys())
# print(min(prices_and_names)) # OK
# print(max(prices_and_names)) #ValueError: max() arg is an empty sequence