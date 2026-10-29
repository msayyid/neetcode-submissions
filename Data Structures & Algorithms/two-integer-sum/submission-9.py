class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = dict()
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in my_map:
                return [my_map[complement], i]
            else:
                my_map[nums[i]] = i

        # my_map = dict()
        # # nums = [3,4,5,6]
        # for i in range(len(nums)):
        #     # my_map[nums[i]] = i
        #     my_map[nums[i]] = my_map.get(nums[i], i)
        #     5:1

        # # my_map = {
        # #     3:0,
        # #     4:1,
        # #     5:2,
        # #     6:3
        # # }
        # # lookup in maps is constant O(1)

        # for i in range(len(nums)):
        #     complement = target - nums[i]
        #     if complement in my_map:
        #         return [i, my_map[complement]]

        



                