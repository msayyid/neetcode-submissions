

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        res = float("inf")

        for i in range(n):
            curSum = 0
            for j in range(i, n):
                curSum += nums[j]
                if curSum >= target:
                    res = min(res, j - i + 1)
                    break

        return 0 if  res == float("inf") else res
        # the_sum = 0
        # l = 0
        # r = 0
        # min_length = float('inf')
        # while r < len(nums):
        #     if sum(nums[l:r]) >= target:
        #         min_length = min(min_length, r - l + 1)
                
        #         r += 1
        #         l = r
        #     else:
        #         r += 1
        # if min_length != float("inf"):
        #     return min_length
        # return 0
        