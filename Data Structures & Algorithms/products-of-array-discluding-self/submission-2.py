class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_mult = [1] * len(nums)
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        product = 1
        for i in range(len(nums)):
            prefix[i] = product
            product *= nums[i]

        product = 1
        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = product
            product *= nums[i]
        
        for i in range(len(nums)):
            prefix_mult[i] = prefix[i] * suffix[i]
        return prefix_mult

        


