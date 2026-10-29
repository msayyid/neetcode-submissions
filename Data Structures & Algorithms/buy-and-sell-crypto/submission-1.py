class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = 0
        sell = 1
        while sell < len(prices):
            # pofitable?
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                max_profit = max(max_profit, profit)
            else:
                buy = sell # if our selling day is less than our buying day we need to change our buying to selling

            sell += 1
        return max_profit