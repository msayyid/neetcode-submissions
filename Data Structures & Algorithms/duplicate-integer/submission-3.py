class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums_map = dict()
        # for i in range(len(nums)):
        #     if nums[i] in nums_map:
        #         return True
        #     else: nums_map[nums[i]] = 1

        # return False
        nums_set = set()
        for i in range(len(nums)):
            if nums[i] in nums_set:
                return True
            else: nums_set.add(nums[i])

        return False