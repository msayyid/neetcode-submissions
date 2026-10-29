class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        for i in range(len(nums)):
            if nums[i] in window:
                return True
            window.add(nums[i])
            if i >= k:
                window.remove(nums[i - k]) # remove the element that is k steps behind current index
        return False