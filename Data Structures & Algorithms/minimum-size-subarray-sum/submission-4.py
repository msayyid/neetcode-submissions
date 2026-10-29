class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float("inf")
        total = 0
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)): # confirm (i think j shoudl start from i, it can't be starting from before i, the window breaks?)
                total += nums[j]
                if total >= target:
                    min_length = min(min_length, j - i + 1)
        
        return 0 if min_length == float("inf") else min_length

