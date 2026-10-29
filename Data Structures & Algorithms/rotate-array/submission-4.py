class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # res = []
        # res = nums[k:] + nums[:k]
        # nums = res
        r = len(nums) - k
        for i in range(k-1):
            nums[i], nums[r] = nums[r], nums[i]
            r += 1

    