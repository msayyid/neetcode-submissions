class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = dict()
        # for i in range(len(nums)):
        #     my_map[nums[i]] = my_map.get(nums[i], i)
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in my_map:
                return [my_map[complement], i]
            my_map[nums[i]] = i
