class TimeMap:

    def __init__(self):
        self.data_structure = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data_structure:
            self.data_structure[key] = []
        self.data_structure[key].append([value, timestamp])
        # print(self.data_structure)
        
    def get(self, key: str, timestamp: int) -> str:
        result = ""
        if key not in self.data_structure:
            return result

        left = 0
        right = len(self.data_structure[key]) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.data_structure[key][mid][1] <= timestamp:
                result = self.data_structure[key][mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return result

