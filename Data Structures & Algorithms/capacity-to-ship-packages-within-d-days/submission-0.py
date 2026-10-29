class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # the ship must be able to carry the heaviest package
        # packages cannot be split
        # any capacity smaller than max(weights) is impossible
        left = max(weights)

        # if the ship can carry the sum of all weights,
        # it can ship every package in a single day
        # therefore, this capacity is guaranteed to work
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2

            # calculate how many days we need at capacity mid
            current = 0
            total_days = 1
            for w in weights:
                current += w

                # if current == mid, the package still fits!!!
                # we only need a new day when capacity is exceeded
                if current > mid:
                    total_days += 1

                    # the package that caused the overflow
                    # must become the first package of
                    # the new day
                    current = w

            # the current capacity is too small
            # we need more than the allowed number of days
            if total_days > days:
                # increase capacity to ship more weight per day
                # mid is invalid, so we can safely eliminate it
                left = mid + 1

            else:
                # current capacity works (total_days <= days)
                # but a smaller capacity might also work
                # keep mid because it could be the minimum
                right = mid

        # left == right
        # this is the minimum capacity that allows us
        # to ship all packages within the allowed days
        return left