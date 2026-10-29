class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        my_map = {0:1} # this is needed to check the lonely elements that are = k
        cur_sum = 0 # keeps record of prefixes
        res = 0 # actual count
        for num in nums:
            cur_sum += num
            diff = cur_sum - k # to look up in the map if we have seen the diff
            res += my_map.get(diff, 1)
            # if diff in my_map: # if yes
            #     res += my_map[diff] # increment the count by my_map[diff] this would mean, this (value) number of starts exist that give valid subarrays that sum to k
            my_map[cur_sum] = my_map.get(cur_sum, 0) + 1 # update the map, if the number doesnt exist create with 1, if does increment by one, the map tell me how many valid  starts exist for this ending
        return res