class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] + nums[i]

        my_map = {0:1}
        count = 0
        for i in range(len(prefix)):
            complement = prefix[i] - k
            if complement in my_map:
                count += my_map[complement]

            my_map[prefix[i]] = my_map.get(prefix[i], 0) + 1

        return count