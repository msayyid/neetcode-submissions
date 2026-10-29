class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = dict()
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in my_map:
                return [i, my_map[complement]] if i < my_map[complement] else [my_map[complement], i]
            else:
                my_map[nums[i]] = i
