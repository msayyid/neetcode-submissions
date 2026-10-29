class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = k - 1
        result = []
        while right < len(nums):
            max_element = max(nums[left:right + 1])
            result.append(max_element)
            left += 1
            right += 1

        return result
