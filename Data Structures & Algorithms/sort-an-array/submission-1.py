import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, low=0, high=len(nums)-1)
        return nums
        
    def quicksort(self, nums, low, high):
        # sorts the elements in the array
        if high <= low: return # base case
        pivot = self.partition(nums, low, high)
        self.quicksort(nums, low, pivot - 1)
        self.quicksort(nums, pivot + 1, high)

    def partition(self, nums, low, high):
        # cuts the array in to two, left and right of the pivot
        pivot_idx = random.randint(low, high)
        nums[pivot_idx], nums[high] = nums[high], nums[pivot_idx]
        
        pivot = nums[high]
        i = low - 1

        for j in range(low, high):
            if nums[j] < pivot:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]

        i += 1
        nums[i], nums[high] = nums[high], nums[i]
        return i

        # pivot = nums[high]
        # i = low - 1
        # for j in range(low, high):
        #     if nums[j] < pivot:
        #         i += 1
        #         nums[i], nums[j] = nums[j], nums[i]
        #         pivot = nums[i]
        # return i # location of pivot