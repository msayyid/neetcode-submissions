class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        left = 0
        right = k - 1

        min_diff = float("inf")
        while right < len(nums):
            diff = nums[right] - nums[left]
            min_diff = min(min_diff, diff)

            left += 1
            right += 1
        return min_diff