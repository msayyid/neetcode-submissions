class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = dict()
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in my_map:
                return [i, nums.index(complement)] if i < nums.index(complement) else [nums.index(complement), i]
            else:
                my_map[nums[i]] = i
