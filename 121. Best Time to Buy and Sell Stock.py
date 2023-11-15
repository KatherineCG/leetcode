# 动态规划
class Solution:
    def maxProfit(self, prices):
        profit = 0
        buyPrice = prices[0]
        for price in prices:
            buyPrice = min(buyPrice, price)
            profit = max(price - buyPrice, profit)

        return profit

if __name__ == '__main__':
    test = Solution()
    prices = [7,6,4,3,1]
    print(test.maxProfit(prices))