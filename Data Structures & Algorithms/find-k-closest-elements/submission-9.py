class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr) - k
        while l < r:
            mid = (l + r) // 2
            if abs(arr[mid] - x) <= abs(arr[mid + k] - x):
                # if left side is closer or tie we discard of the right side
                r = mid
            else:
                # if right side is closer to be a starting point we discard of the left side
                l = mid + 1
            
        return arr[l:l+k]


