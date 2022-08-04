class Solution:
    def maxProfit(self, prices) -> int:
        buy = 0
        sell = 1
        profit = 0
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                if profit < prices[sell] - prices[buy]:
                    profit = prices[sell] - prices[buy]
                sell = sell + 1
            else:
                buy =  sell
                sell = sell + 1
        return profit

a = Solution()
print(a.maxProfit(prices = [7,1,5,3,6,4]))