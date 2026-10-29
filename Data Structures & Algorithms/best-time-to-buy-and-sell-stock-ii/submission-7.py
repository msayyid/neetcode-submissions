# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         total = 0
#         for i in range(len(prices)-1):
#             total += max(prices[i+1] - prices[i], 0)
#         return total

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            # if prices[i+1] - prices[i] > 0:
            #     profit += prices[i+1] - prices[i]
            profit += max(prices[i+1] - prices[i], 0)
        return profit