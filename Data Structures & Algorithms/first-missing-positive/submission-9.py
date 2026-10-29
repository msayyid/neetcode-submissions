class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        while i < n:
            # correct index
            correct = nums[i] - 1 #  3 : 2; 8 : 7; 1 : 0
            if 1 <= nums[i] <= n and nums[i] != nums[correct]:
                # swap
                nums[i], nums[correct] = nums[correct], nums[i]

            else:
                i += 1
        
        for i in range(n): # 0, 1, 2 ....
            if nums[i] != i + 1: # do i have 1 at i = 0, do i have 2 at i = 1
                return i + 1
        return n + 1