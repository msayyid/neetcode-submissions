class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        the_sum = 0
        l = 0
        r = 0
        min_length = float('inf')
        while r < len(nums):
            if sum(nums[l:r]) >= target:
                min_length = min(min_length, r - l + 1)
                
                r += 1
                l = r
            else:
                r += 1
        if min_length != float("inf"):
            return min_length
        return 0
        