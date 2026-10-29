class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = k - 1
        result = []
        max_element = nums[0]
        while right < len(nums):
            for i in range(left, right + 1):
                max_element = max(max_element, nums[i])
            # max_element = max(nums[left:right + 1])
            result.append(max_element)
            left += 1
            right += 1

        return result