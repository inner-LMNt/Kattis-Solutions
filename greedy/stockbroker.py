days = int(input())

stocks = []
for i in range(days):
    stocks.append(int(input()))

shares = 0
money = 100

for i in range(days - 1):
    current_stock = stocks[i]
    next_stock = stocks[i+1]

    if current_stock < next_stock:
        # If price will increase, buy as many shares as possible until max 100000 shares
        if money >= current_stock:
            max_shares = 100000 - shares
            shares_to_buy = min(max_shares, money // current_stock)
            shares += shares_to_buy
            money -= shares_to_buy * current_stock
    elif current_stock > next_stock:
        # If price will decrease, sell all shares
        money += shares * current_stock
        shares = 0

# Sell everything on last day
money += shares * stocks[-1]

print(money)
