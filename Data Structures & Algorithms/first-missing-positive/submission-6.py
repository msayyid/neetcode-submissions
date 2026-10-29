class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # my_map = dict()
        # for i in range(len(nums)):
        #     my_map[nums[i]] = my_map.get(nums[i], 0) + 1
        
        # for k, v in my_map.items():
        #     complement = k 
        # nums.sort()
        nums_set = set(nums)
        count = 1
        for i in range(len(nums)):
            if count not in nums_set:
                return count
            count += 1
        return count
            # if num + 1 not in nums_set:
            #     if num+1 > 0:
            #         return num+1


