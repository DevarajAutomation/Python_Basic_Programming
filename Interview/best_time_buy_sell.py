"""https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/"""


def best_time_to_sell(prices):
    buy = prices[0]

    profit = 0

    for sell in prices[1:]:
        if sell > buy:
            profit = max(profit, sell - buy)
        else:
            buy = sell

    return profit

prices=[1,5,7,8,2,1]

print(best_time_to_sell(prices))
