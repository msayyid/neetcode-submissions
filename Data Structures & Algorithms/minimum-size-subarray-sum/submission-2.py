class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        l = 0
        min_length = float("inf")
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                min_length = min(min_length, r - l + 1)
                total -= nums[l]
                l += 1
        if min_length == float("inf"):
            return 0
        return min_length


        # n = len(nums)
        # res = float("inf")

        # for i in range(n):
        #     curSum = 0
        #     for j in range(i, n):
        #         curSum += nums[j]
        #         if curSum >= target:
        #             res = min(res, j - i + 1)
        #             break

        # return 0 if  res == float("inf") else res
        