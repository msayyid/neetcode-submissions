class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        result = []

        bucket = [[] for _ in range(len(nums) + 1)]

        # fill the bucket
        for key, val in count.items():
            bucket[val].append(key)

        for i in range(len(bucket) - 1, -1, -1):
            for j in range(len(bucket[i])):
                result.append(bucket[i][j])
                if len(result) == k:
                    return result
        # take top k elements from the back of the 
        # print(bucket)