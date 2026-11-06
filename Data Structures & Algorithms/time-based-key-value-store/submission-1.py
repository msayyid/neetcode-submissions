class TimeMap:

    def __init__(self):
        self.my_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.my_map:
            self.my_map[key].append((value, timestamp))
        else:
            self.my_map[key] = []
            self.my_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        if key not in self.my_map:
            return result
        left = 0
        right = len(self.my_map[key]) - 1

        while left <= right:
            mid = (left + right) // 2
            
            if self.my_map[key][mid][1] <= timestamp:
                result = self.my_map[key][mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return result
        
