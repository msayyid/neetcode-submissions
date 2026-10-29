class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = dict()

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in my_map:
                # if complement is in the map which it is not yet
                # return the value (index) of it and the index of the current i
                # sum of values of which give target
                return [my_map[complement], i]
            else:
                # otherwise create a key and a value of the current value in array to the map
                my_map[nums[i]] = i