class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # i could create a map and store teh values as keys and their appearnce as values
        # and return whichever element appears more than n/2 times in the array
        count = 1
        majority_num = nums[0]
        for i in range(1, len(nums)):
            if majority_num == nums[i]:
                count += 1
            else: count -= 1
            
            if count == 0:
                majority_num = nums[i]
                count = 1
        return majority_num