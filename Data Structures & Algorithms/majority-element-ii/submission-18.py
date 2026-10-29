class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # at most 2 elements are possible to be in a result
        # because of n//3, which makes it impossible for more than
        # two elements be greater than the third of the length of nums

        cand1 = None
        cand2 = None
        # None helps us avoid crashes, if there are fewer than 2 elements
        count1 = 0
        count2 = 0
        for i in range(len(nums)):
            if nums[i] == cand1:
                count1 += 1
            elif nums[i] == cand2:
                count2 += 1
            elif count1 == 0:
                cand1 = nums[i]
                count1 = 1
            elif count2 == 0:
                cand2 = nums[i]
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        
        count1 = count2 = 0
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1

        # verification
        n = len(nums)
        res = []
        if count1 > n // 3:
            res.append(cand1)
        if count2 > n // 3:
            res.append(cand2)
        return res
            