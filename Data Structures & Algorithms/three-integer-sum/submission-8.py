class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        print(nums)
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            cur_sum = 0
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                if cur_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    break
                    
                elif cur_sum > 0:
                    right -= 1
                else:
                    left += 1
        return result