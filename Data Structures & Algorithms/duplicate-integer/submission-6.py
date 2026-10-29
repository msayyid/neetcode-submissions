class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_map = dict()
        for i in range(len(nums)):
            my_map[nums[i]] = my_map.get(nums[i], 0) + 1
        
        for k, v in my_map.items():
            if v > 1:
                return True
        return False
        