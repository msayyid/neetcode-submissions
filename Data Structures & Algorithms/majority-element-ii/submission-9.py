class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        the_one = 0
        the_two = 1
        count1 = 0
        count2 = 0
        for i in range(len(nums)):
            if nums[i] == nums[the_one]:
                count1 += 1
            elif nums[i] == nums[the_two]:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
                if count1 == 0  and nums[the_one] != nums[the_two]:
                    the_one = i
                    count1 = 1
                if count2 == 0 and nums[the_one] != nums[the_two]:
                    the_two = i
                    count2 = 1
        count1 = 0
        count2 = 0
        # for i in range(len(nums)):
        #     if nums[i] == nums[the_one]:
        #         count1 += 1
        #     elif nums[i] == nums[the_two]:
        #         count2 += 1

        if nums:
            for i in range(len(nums)):
                if nums[i] == nums[the_one]:
                    count1 += 1
                elif nums[i] == nums[the_two]:
                    count2 += 1

            if count1 > len(nums)//3 and count2 > len(nums)//3:
                return [nums[the_one], nums[the_two]]
            elif count1 > len(nums)//3 and count2 <= len(nums)//3:
                return [nums[the_one]]
            elif count1 <= len(nums)//3 and count2 > len(nums)//3:
                return [nums[the_two]]
        return []
            