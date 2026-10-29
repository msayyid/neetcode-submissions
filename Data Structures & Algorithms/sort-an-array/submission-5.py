class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            left = merge_sort(left)
            right = merge_sort(right)


            # we have now split it, now we need to merge
            i = 0
            j = 0
            sorted_arr = []

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    sorted_arr.append(left[i])
                    i += 1

                else:
                    sorted_arr.append(right[j])
                    j += 1

            while i < len(left):
                sorted_arr.append(left[i])
                i += 1

            while j < len(right):
                sorted_arr.append(right[j])
                j += 1

            return sorted_arr

        return merge_sort(nums)