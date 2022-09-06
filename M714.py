#Best Time to Buy and Sell Stock with Transaction Fee

prices = [1,3,2,8,4,9]
fee = 2


def maxProfit(prices, fee):
    cash, hold = 0, -prices[0]
    for i in range(1, len(prices)):
        cash = max(cash, hold + prices[i] - fee)
        hold = max(hold, cash - prices[i])
    return cash

print(maxProfit(prices,fee))