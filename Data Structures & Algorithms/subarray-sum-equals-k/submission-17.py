class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        my_map = {0:1}
        prefix = 0
        count = 0
        for i in range(len(nums)):
            prefix += nums[i]
            complement = prefix - k
            if complement in my_map:
                count += my_map[complement]
            my_map[prefix] = my_map.get(prefix, 0) + 1
        return count