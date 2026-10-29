class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_map = dict()
        for i in range(len(nums)):
            if nums[i] in nums_map.keys():
                return True
            else: nums_map[nums[i]] = 1

        return False