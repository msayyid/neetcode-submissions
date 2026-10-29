class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # i could create a map and store teh values as keys and their appearnce as values
        # and return whichever element appears more than n/2 times in the array
        my_map = dict()
        for i in range(len(nums)):
            my_map[nums[i]] = my_map.get(nums[i], 0) + 1
        
        for key, value in my_map.items():
            if value > len(nums) / 2:
                return key