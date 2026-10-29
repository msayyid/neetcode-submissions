class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)

        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]

        min_length = float("inf")
        # nums =      [2,1,5,1,5,3]
        # prefixSum = [0,2,3,8,9,14,17]
        #             [0,1,2,3,4, 5, 6]

        for i in range(n):
            l, r = i, n
            while l < r:
                mid = (l + r) // 2
                cur_sum = prefix[mid + 1] - prefix[i]
                if cur_sum >= target:
                    r = mid
                else:
                    l = mid + 1
            if l != n:
                min_length = min(min_length, l - i + 1)
        
        if min_length == float("inf"):
            return 0
        return min_length



        # l, total = 0, 0
        # min_length = float("inf")
        # for r in range(len(nums)):
        #     total += nums[r]
        #     while total >= target:
        #         min_length = min(min_length, r - l + 1)
        #         # in here we are reducing total because we need to check if 
        #         # there's a shorter window sum of which is valid
        #         total -= nums[l]
        #         l += 1
            
        # if min_length == float("inf"):
        #     return 0
        # return min_length