class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, quad = [], []

        def k_sum(k, start, target):
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    quad.append(nums[i]) # in here, if i understand correctly, we are appending the first starting fo the first possible solution
                    k_sum(k - 1, i + 1, target - nums[i]) # then we are calling k_sum again but with k - 1, meaning if it was 4 sum this one would be called for 3 sum, and target, i don't knwo why it is target - nums[i]
                    # if we said target - nums[i] is new target i think it would mean like, we would have to for example find the number that would in sum return i don't know i am confused in here

                    quad.pop() # and i don't know what is this for either
                return # this one as well

            # in here we start the base case, when k is equal to two
            # we can start our two pointer approach
            l, r = start, len(nums) - 1 # i don't know why l is start
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.append(quad + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1 # i dont know why we are decrementing r as well here only l, i think it gets handled by the > case above
        k_sum(4, 0, target)
        return res

