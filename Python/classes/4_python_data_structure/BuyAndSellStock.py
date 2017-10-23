# Say you have an array for which the ith element is the price of
#   a given stock on day i.
#
# If you were only permitted to complete at most one transaction
#   (ie, buy one and sell one share of the stock), design an algorithm to find
#   the maximum profit.

# Example 1:
# Input: [7, 1, 5, 3, 6, 4]
# Output: 5
#
# max. difference = 6-1 = 5 ( not 7-1 = 6, short-selling is not allowed :-( )
#
# Example 2:
# Input: [7, 6, 4, 3, 1]
# Output: 0
#
# In this case, no transaction is done, i.e. max profit = 0.
def maxProfit(prices):
    minPrice = 9999999999
    minPrices = [minPrice]
    for p in prices:
        if p < minPrice:
            minPrice = p
        minPrices.append(minPrice)
    # print len(prices)
    # print len(minPrices)

    maxProfit = 0 #
    # for i in range(len(prices)):
    #     profit = prices[i] - minPrices[i]
    #     if profit >  maxProfit:
    #         maxProfit = profit
    # return maxProfit
    # minPrices.pop()
    while len(prices) > 0:
        lastPrice = prices.pop()
        lastMinPrice = minPrices.pop()
        profit = lastPrice - lastMinPrice
        # profit = ((prices.pop()) - (minPrices.pop()))
        if profit >  maxProfit:
            maxProfit = profit
    return maxProfit


print maxProfit([7, 1, 5, 3, 6, 4])
# print maxProfit([7, 6, 4, 3, 1])
