class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        count = 0
        for n in nums:
            if n-1 not in numSet:
                # count += 1
                count = 0
                while n+count in numSet:
                    count += 1
                longest = max(longest, count)
        return longest


        
        # my_set = set(nums)
        # longest = 0
        # for n in nums:
        #     if n - 1 not in my_set:
        #         length = 0
        #         while n + length in my_set:
        #             length += 1
        #         longest = max(length, longest)
        # return longest