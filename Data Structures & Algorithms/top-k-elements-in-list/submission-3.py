import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # map nums to map
        my_map = dict()
        freq = []
        for i in range(len(nums)):
            my_map[nums[i]] = my_map.get(nums[i], 0) + 1

        
        for i in range(len(nums) + 1):
            # we need + 1 because of the index nature which starts from 0? (correct me)
            freq.append([])

        for key, val in my_map.items():
            freq[val].append(key)
            # now we're filling the lists of our freq list
        
        result = []
        for i in range(len(freq)-1, 0, -1):
            for j in range(len(freq[i])):
                result.append(freq[i][j])
                if len(result) == k:
                    return result