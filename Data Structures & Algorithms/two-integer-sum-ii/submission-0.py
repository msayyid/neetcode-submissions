class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(len(numsers)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        return [i, j]