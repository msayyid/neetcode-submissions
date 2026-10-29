class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            mid = (left + right) // 2
            total_hours = 0

            for p in piles:
                total_hours += math.ceil(p / mid)
            # if total hours is greater than allowed hours
            # we need to east faster
            if total_hours > h:
                left = mid + 1
            
            else:
                right = mid
        return left