class Solution:
    def mySqrt(self, x: int) -> int:

        # sqaure roots fo 0 and 1 are themselves
        if x <= 1:
            return x
        left = 1
        right = x

        # search for the integer square root in [1, x]
        while left < right:
            mid = (left + right) // 2

            if mid * mid == x:
                # perfect square found
                return mid
            
            elif mid * mid > x:
                # mid is too large
                # keep mid because it could be the first number
                # whose square is greater than x
                right = mid

            else:
                # mid is too small
                # exclude mid and all smaller numbers
                left = mid + 1
        
        # loop ends when left == right
        # if no perfect square was found, left is the 
        # smallest integer whose square is greater than x
        # therefore, left - 1 is the largest integer
        # whose square is less than x
        return left - 1