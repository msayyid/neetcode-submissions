class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        # print(freq)


        my_map = {}
        for num in nums:
            my_map[num] = my_map.get(num, 0) + 1

        # print(my_map)
        for key, val in my_map.items():
            freq[val].append(key)
        # print(freq)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res