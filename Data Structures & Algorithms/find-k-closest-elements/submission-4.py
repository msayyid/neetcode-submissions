class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr) - k # because we need room for the k elemtns if 
                         # r is a starting point

        while l < r:
            mid = (l + r) // 2
            # we are checking where this window must move l or r
            # if mid is closer to x mid must stay and r must decrement
            # if mid + k (right outside the window) is closer to x
            # we need to move our l or mid (or starting of our window)
            # why what guarantees shit i am so ocnfused right now
            if abs(arr[mid] - x) <= abs(arr[mid + k] - x): # if our mid is more fit to be i am confused 
                r = mid
            else:
                l = mid + 1 # why plus one? why are we not cutting the remaining half in 2?
        return arr[l:l+k]

