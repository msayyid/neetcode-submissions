class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        # print(nums)
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            # cur_sum = 0
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                if cur_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    right -= 1
                    while right > left and nums[right] == nums[right + 1]:
                        right -= 1
                    
                elif cur_sum > 0:
                    right -= 1
                else:
                    left += 1
        return result