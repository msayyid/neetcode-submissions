class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        my_map = dict()
        my_map[0] = 1
        prefix = 0
        count = 0
        for num in nums:
            prefix += num
            if prefix - k in my_map:
                count += my_map[prefix-k]
            my_map[prefix] = my_map.get(prefix, 0) + 1
        return count