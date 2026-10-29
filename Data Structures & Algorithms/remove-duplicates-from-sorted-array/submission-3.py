class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        # j = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[k] = nums[i]
                k += 1
            if i+1 == len(nums)-1:
                nums[k] = nums[i+1]
        return k+1

