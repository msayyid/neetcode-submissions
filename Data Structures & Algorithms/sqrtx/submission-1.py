class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        if x == 1:
            return 1

        left = 1
        right = x

        while left < right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            
            elif mid * mid > x:
                right = mid

            else:
                left = mid + 1

        return left - 1 if left == right else left