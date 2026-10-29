class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        longest = 0
        count = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                count += 1
            elif nums[i] - nums[i-1] > 1:
                longest = max(longest, count)
                count = 1
        
        return max(longest, count)


        
        # my_set = set(nums)
        # longest = 0
        # for n in nums:
        #     if n - 1 not in my_set:
        #         length = 0
        #         while n + length in my_set:
        #             length += 1
        #         longest = max(length, longest)
        # return longest