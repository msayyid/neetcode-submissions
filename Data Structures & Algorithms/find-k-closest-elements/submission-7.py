class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr) - 1 # -1 because of the 0 indexed nature of arrays
        while r - l + 1 > k:
            left_dist = abs(x - arr[l])
            right_dist = abs(x - arr[r])
            if left_dist <= right_dist: # if left is closer to x or a tie
                # we move right pointer
                r -= 1
            else: # else if right dist is closer to x we do not need left as a starting point for us
                # so we move left
                l += 1
        return arr[l:k + 1]



