class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        min_speed = right
        while left <= right:
            mid = (left + right) // 2

            # now calculate the overall time
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile / mid)

            if total_time <= h:
                right = mid - 1
                min_speed = min(min_speed, mid)
            else:
                left = mid + 1

        return min_speed
