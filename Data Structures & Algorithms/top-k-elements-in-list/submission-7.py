class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket search thing
        bucket = [[] for _ in range(len(nums) + 1)]
        # print(bucket)
        # since we cannot really have more frequencey than
        # the len(nums), we could store the numbers that are repeated
        # bucket[i]th time in bucket[i]th bucket

        freq = Counter(nums)
        for key, val in freq.items():
            bucket[val].append(key)
        # print(bucket)
        res = []

        for i in range(len(bucket) - 1, 0, -1):
            for b in bucket[i]:
                res.append(b)
                if len(res) == k:
                    return res
