class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        n = len(nums)
        # l, r = 0, len(nums) - 1
        # while l < r:
        #     nums[l], nums[r] = nums[r], nums[l]
        #     l += 1
        #     r -= 1

        # l, r = 0, k - 1
        # while l < r:
        #     nums[l], nums[r] = nums[r], nums[l]
        #     l += 1
        #     r -= 1

        # l, r = k, len(nums) - 1
        # while l < r:
        #     nums[l], nums[r] = nums[r], nums[l]
        #     l += 1
        #     r -= 1

        def reverse(l, r, n):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1
        reverse(0, n - 1, n)
        reverse(0, k - 1, n)
        reverse(k, n - 1, n)