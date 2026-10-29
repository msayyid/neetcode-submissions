class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        j = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[j]:
                nums[k] = nums[i]
                k += 1
            if j == len(nums)-1:
                nums[k] = nums[j]
                # k+= 1
            j += 1
        return k+1

