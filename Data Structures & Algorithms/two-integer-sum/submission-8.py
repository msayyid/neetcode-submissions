class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        my_map = dict()
        # nums = [3,4,5,6]
        for i in range(len(nums)):
            # my_map[nums[i]] = i
            my_map[nums[i]] = my_map.get(nums[i], i)
        # my_map = {
        #     3:0,
        #     4:1,
        #     5:2,
        #     6:3
        # }
        # lookup in maps is constant O(1)

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in my_map:
                return [i, my_map[complement]]

        



                