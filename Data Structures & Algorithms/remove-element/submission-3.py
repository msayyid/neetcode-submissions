class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pointer1 = 0
        pointer2 = len(nums) - 1
        count = 0
        if len(nums) == 0:
            return 0
        for i in range(len(nums)):
            if pointer1 < pointer2:
                if nums[pointer1] == val and nums[pointer2] != val:
                    nums[pointer1], nums[pointer2] = nums[pointer2], nums[pointer1]
                    count += 1
                    pointer1 += 1
                    pointer2 -=1
                elif nums[pointer1] == val and nums[pointer2] == val:
                    pointer2 -= 1
                elif nums[pointer1] != val and nums[pointer2] == val:
                    pointer2 -= 1
                else:
                    pointer1 += 1
                    pointer2 += 1


        return len(nums[:nums.index(val)])