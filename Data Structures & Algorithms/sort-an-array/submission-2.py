# # bubble sort (On^2) O(1)

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        n = len(nums)

        for i in range(n):
            for j in range(n - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums
