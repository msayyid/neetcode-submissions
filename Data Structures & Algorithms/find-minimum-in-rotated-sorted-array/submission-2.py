class Solution:
    def findMin(self, nums: list[int]) -> int:
        # Search for the minimum in the rotated sorted array.
        left = 0
        right = len(nums) - 1

        # Continue until only one candidate remains.
        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[right]:
                # The portion from mid to right is sorted.
                # Everything after mid is greater than nums[mid].
                # The minimum must be at mid or somewhere to its left.
                # Keep mid because it could be the minimum.
                right = mid

            elif nums[mid] > nums[right]:
                # There is a rotation break between mid and right.
                # The minimum must be strictly to the right of mid.
                # Exclude mid and everything before it.
                left = mid + 1

        # The loop ends when left == right.
        # Only one candidate remains, which must be the minimum.
        # Return the value, not its index.
        return nums[left]