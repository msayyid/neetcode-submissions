class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        total = 0
        for i in range(len(nums)):
            total = 0
            if nums[i] == k:
                    count += 1
            total += nums[i]
            for j in range(i+1, len(nums)):
                total += nums[j]
                if total == k:
                    count += 1
        return count