class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr) - 1
        while r - l + 1 > k:
            left_dist = abs(arr[l] - x)
            right_dist = abs(x - arr[r])
            if left_dist < right_dist: # if left is closer
                r -= 1
            elif left_dist == right_dist: # if a tie (both numbers are on the same distance from x)
                r -= 1
            else: # if right side is closer
                l += 1

        print("right pointer - ", r)
        print("left pointer - ", l)
        return arr[l:r+1]
