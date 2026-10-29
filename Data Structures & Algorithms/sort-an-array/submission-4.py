class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums)

    def merge_sort(self, nums):
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        sorted_left = self.merge_sort(nums[:mid])
        sorted_right = self.merge_sort(nums[mid:])

        return self.merge(sorted_left, sorted_right)

    def merge(self, A, B):
        result = []
        i = 0
        j = 0
        while i < len(A) and j < len(B):
            if A[i] <= B[j]:
                result.append(A[i])
                i += 1
            else:
                result.append(B[j])
                j += 1
        
        while i < len(A):
            result.append(A[i])
            i += 1

        while j < len(B):
            result.append(B[j])
            j += 1
        
        return result