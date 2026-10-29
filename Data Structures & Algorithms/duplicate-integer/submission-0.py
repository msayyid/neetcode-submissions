class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_map = Counter(nums)
        print(my_map)
        yes = True
        for key, value in my_map.items():
            if value > 1:
                return True
        return False