class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        temp = []
        res = []
        for a in range(n):
            for b in range(n):
                for c in range(n):
                    for d in range(n):
                        if a != b and b != c and a != c and c != d  and b != d and a != d:
                            temp = []
                            if nums[a] + nums[b] + nums[c] + nums[d] == target:
                                temp.append(nums[a])
                                temp.append(nums[b])
                                temp.append(nums[c])
                                temp.append(nums[d])
                                temp.sort()
                                if temp not in res:
                                    res.append(temp)
        return res