# Task 2
# Create a function which takes as input two dicts with structure
# mentioned above, then computes and returns the total price of stock.

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# for me: print(stock['banana'], type(stock['banana']))
# fro me: print(prices['banana'], type(prices['banana']))


def fruit_shop(stock_quantity, fruit_price):
    for fruit in stock:
        amount_total = stock[fruit] * prices[fruit]
        print('Total price of ' + fruit + "s " + 'stock is: ' + str(amount_total) + ' some kind of currency.')


fruit_shop(stock, prices)
