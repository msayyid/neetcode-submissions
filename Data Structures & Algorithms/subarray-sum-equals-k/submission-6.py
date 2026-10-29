class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        my_map = {0:1}
        cur_sum = 0
        res = 0
        for num in nums:
            cur_sum += num
            diff = cur_sum - k
            if diff in my_map:
                res += my_map[diff]
            my_map[cur_sum] = my_map.get(cur_sum, 0) + 1
        return res