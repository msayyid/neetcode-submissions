class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        total = 0
        min_length = float("inf")
        while r < len(nums):
            total += nums[r]
            while total >= target: # keep shrinking the window if total meets the target
                min_length = min(min_length, r - l + 1)
                total -= nums[l]
                l += 1
            r += 1
            
        if min_length == float("inf"): return 0
        return min_length