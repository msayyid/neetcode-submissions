class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mymap = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in mymap:
                return [mymap[complement], i]
            mymap[nums[i]] = i

        