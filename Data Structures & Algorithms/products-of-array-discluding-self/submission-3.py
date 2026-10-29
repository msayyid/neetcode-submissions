class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_mult = [1] * len(nums)
        # prefix = [1] * len(nums)
        # suffix = [1] * len(nums)
        product = 1
        for i in range(len(nums)):
            prefix_mult[i] = product
            product *= nums[i]

        product = 1
        for i in range(len(nums) - 1, -1, -1):
            prefix_mult[i] *= product
            product *= nums[i]

        return prefix_mult

        


