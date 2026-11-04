class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2

            # target found
            if nums[mid] == target:
                return True

            # duplicate issue
            # if nums[left] == nums[mid], we cannot surely tell which half is sorted
            # since nums[mid] != target nums[left] is also not target,
            # so it is safe to discard nums[left].
            if nums[left] == nums[mid]:
                left += 1

            else:
                # left half is sorted
                if nums[left] < nums[mid]:

                    # if target is inside the sorted left half
                    # discard the right half
                    if nums[left] <= target < nums[mid]:
                        right = mid - 1

                    # otherwise target is in the other half
                    else:
                        left = mid + 1

                # if nums[left] > nums[mid],
                # the rotation must be on the left side,
                # so the right half is sorted
                else:

                    # if target lies inside the sorted right half,
                    # discard the left half
                    if nums[mid] < target <= nums[right]:
                        left = mid + 1

                    # otherwise target must be in the other half
                    else:
                        right = mid - 1
        return False