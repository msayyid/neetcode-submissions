import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = dict()
        for i in range(len(nums)):
            my_map[nums[i]] = my_map.get(nums[i], 0) + 1

        
        heap = []
        
        for key, val in my_map.items():

            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)
        result = []
        for el in heap:
            result.append(el[1])

        return result


        


        