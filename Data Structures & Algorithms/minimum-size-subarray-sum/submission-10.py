class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        min_length = float("inf")
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                min_length = min(min_length, r - l + 1)
                # in here we are reducing total because we need to check if 
                # there's a shorter window sum of which is valid
                total -= nums[l]
                l += 1
            
        if min_length == float("inf"):
            return 0
        return min_length