class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set()
        my_set.add(n for n in nums)

        res = []
        for n in nums:
            if n - 1 not in nums:
                start = n - 1
                res.append(start)
            else: continue 

            if start + 1 in nums:
                # res.append(start)
                res.append(start + 1)
        return len(res)