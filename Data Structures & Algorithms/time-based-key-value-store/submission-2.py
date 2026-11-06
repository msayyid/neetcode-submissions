class TimeMap:

    def __init__(self):
        # dict where each key maps to a list of (value, timestamp) tuples
        self.my_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.my_map:
            self.my_map[key] = []
        
        # append the new value and its timestamp
        # timestamps are strictly increasing
        # so the list remains sorted without needing to sort it
        self.my_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:

        result = ""
        if key not in self.my_map:
            return result
        
        # binary search through the timestamps stored for this key
        left = 0
        right = len(self.my_map[key]) - 1

        # use <= because we must check the last remaining candidate
        # our pointer updates eliminate mid using mid + 1 or mid - 1
        while left <= right:
            mid = (left + right) // 2
            
            if self.my_map[key][mid][1] <= timestamp:
                # the stored timestamp is <= the requested timestamp
                # this is a valid candidate, but it might not be
                # the most recent valid value.
                # save the value before moving left
                # even if we don't find a better timestamp,
                # we won't lose the valid answer
                result = self.my_map[key][mid][0]
                left = mid + 1

            else:
                # stored timestamp is greater than requested
                # this valeu is too recent and cannot be returned
                # search left
                right = mid - 1
        return result
        
