class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        # print(intervals)

        res = [intervals[0]]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            # check if the current interval overlaps with 
            # the last merged one
            if start <= res[-1][1]:
                # extend the ending point if needed
                res[-1][1] = max(res[-1][1], end)

            # no overalps so just append a new one
            else:
                res.append([start, end])
        return res