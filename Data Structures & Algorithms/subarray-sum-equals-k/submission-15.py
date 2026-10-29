class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix = [0] * len(nums)
        # prefix[0] = nums[0]
        # for i in range(1, len(nums)):
            # prefix[i] = prefix[i - 1] + nums[i]

        prefix = 0
        my_map = {0:1}
        count = 0
        for i in range(len(nums)):
            prefix += nums[i]
            # complement = prefix - k
            if prefix - k in my_map:
                count += my_map[prefix - k]

            my_map[prefix] = my_map.get(prefix, 0) + 1

        return count