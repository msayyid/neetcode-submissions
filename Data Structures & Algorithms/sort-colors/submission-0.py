class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        my_map = dict()
        for i in range(len(nums)):
            my_map[nums[i]] = my_map.get(nums[i], 0) + 1
        
        counter = 0
        for i in range(3):
            if i in my_map:

                for j in range(my_map[i]):
                    nums[counter] = i
                    counter += 1
            else:
                continue