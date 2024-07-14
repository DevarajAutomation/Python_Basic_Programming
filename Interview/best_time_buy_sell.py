"""https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/"""

def best_to_by_sell_stock(prices):
    profit=0
    buy=prices[0]

    for sell in prices[1:]:
        if sell > buy:
            profit=max(profit,sell-buy)

        else:
            buy=sell

    return profit

prices = [7,1,5,3,6,4]

print(best_to_by_sell_stock(prices))