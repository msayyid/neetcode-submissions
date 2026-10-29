class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()
        for i in range(n):
            l, r = i + 1, n - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while l < r:
                target = nums[l] + nums[r] + nums[i]
                if target == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    r -= 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
                elif target > 0:
                    r -= 1
                else:
                    l += 1
        return res
        

