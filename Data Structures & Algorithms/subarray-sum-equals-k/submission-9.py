class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        my_map = {0:1}
        count = 0
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            complement = total - k
            if complement in my_map:
                count += my_map[complement]

            my_map[total] = my_map.get(total, 0) + 1

        return count