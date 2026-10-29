class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        res, quad = [], []

        def k_sum(k, start, target):
            # if k is not 2 yet, we still need to choose more numbers
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    # skip duplicates at the current recursion level
                    if i > start and nums[i] == nums[i - 1]:
                        continue

                    # choose nums[i] as one part of the current answer
                    quad.append(nums[i])

                    # we already picked nums[i], so now we need:
                    # (k - 1) more numbers
                    # starting only from i + 1
                    # whose sum must be (target - nums[i])
                    k_sum(k - 1, i + 1, target - nums[i])

                    # backtrack 
                    # remove the number we just picked
                    # so we can try the next possible choice
                    quad.pop()
                
                # important:
                # once this recursive level finishes its loop, stop here
                # and do not continue into the 2-pointer code below
                return

            # base case: k == 2
            # now the problem is just 2Sum in a sorted array
            l, r = start, len(nums) - 1
            while l < r:
                pair_sum = nums[l] + nums[r]
                if pair_sum < target:
                    l += 1
                elif pair_sum > target:
                    r -= 1
                else:
                    # quad already has the previously chosen numbers
                    # nums[l] and nums[r] complete the combination
                    res.append(quad + [nums[l], nums[r]])

                    l += 1
                    # skip duplicate left values
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        k_sum(4, 0, target)
        return res
        # nums.sort()
        # res, quad = [], []

        # def k_sum(k, start, target):
        #     if k != 2:
        #         for i in range(start, len(nums) - k + 1):
        #             if i > start and nums[i] == nums[i - 1]:
        #                 continue
        #             quad.append(nums[i]) # in here, if i understand correctly, we are appending the first starting fo the first possible solution
        #             k_sum(k - 1, i + 1, target - nums[i]) # then we are calling k_sum again but with k - 1, meaning if it was 4 sum this one would be called for 3 sum, and target, i don't knwo why it is target - nums[i]
        #             # if we said target - nums[i] is new target i think it would mean like, we would have to for example find the number that would in sum return i don't know i am confused in here

        #             quad.pop() # and i don't know what is this for either
        #         return # this one as well

        #     # in here we start the base case, when k is equal to two
        #     # we can start our two pointer approach
        #     l, r = start, len(nums) - 1 # i don't know why l is start
        #     while l < r:
        #         if nums[l] + nums[r] < target:
        #             l += 1
        #         elif nums[l] + nums[r] > target:
        #             r -= 1
        #         else:
        #             res.append(quad + [nums[l], nums[r]])
        #             l += 1
        #             while l < r and nums[l] == nums[l - 1]:
        #                 l += 1 # i dont know why we are decrementing r as well here only l, i think it gets handled by the > case above
        # k_sum(4, 0, target)
        # return res

