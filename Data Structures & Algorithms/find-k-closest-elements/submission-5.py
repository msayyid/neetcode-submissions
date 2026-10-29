class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr) - k # because we need room for the k elemtns if 
                         # r is a starting point

        while l < r:
            # pick a middle starting point to test
            mid = (l + r) // 2

            # we compare the first element of this window (arr[mid])
            # with the very next element after this window (arr[mid + k])

            if abs(arr[mid] - x) <= abs(arr[mid + k] - x): 
                # if the element at "mid" is closer to x (or it is a tie),
                # our best window cannot start any further to the right
                # so we bring the right boundary r to mid
                r = mid
            else:
                # if the element at mid + k is closer to x, it means
                # the current mid is a bad start. we should shift right
                l = mid + 1 # we move the left pointer to the next of mid and cut the current l and r in half
        
        # after the loop, l has found the best possible starting index
        # return k elements starting from that index
        return arr[l:l+k]

