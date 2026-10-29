class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        the_one = nums[0]
        the_two = nums[1]
        count1 = 0
        count2 = 0
        for i in range(len(nums)):
            if nums[i] == the_one:
                count1 += 1
            elif nums[i] == the_two:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
                if count1 == 0  and the_one != the_two:
                    the_one = nums[i]
                    count1 = 1
                if count2 == 0 and the_one != the_two:
                    the_two = nums[i]
                    count2 = 1
        count1 = 0
        count2 = 0

        if nums:
            for i in range(len(nums)):
                if nums[i] == the_one:
                    count1 += 1
                elif nums[i] == the_two:
                    count2 += 1

            if count1 > len(nums)//3 and count2 > len(nums)//3:
                return [the_one, the_two]
            elif count1 > len(nums)//3 and count2 <= len(nums)//3:
                return [the_one]
            elif count1 <= len(nums)//3 and count2 > len(nums)//3:
                return [the_two]
        return []
            