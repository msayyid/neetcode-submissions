class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        for i in range(len(prices)-1):
            diff_check = prices[i+1] - prices[i]
            if diff_check > 0:
                total += diff_check
        return total