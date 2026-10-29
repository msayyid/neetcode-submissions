class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()
        for i in range(1, n):
            l, r = i + 1, n - 1
            if nums[i] == nums[i - 1]:
                continue
            while l < r:
                target = nums[l] + nums[r] + nums[i]
                if target == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                elif target > 0:
                    r -= 1
                else:
                    l += 1
        return res
        

