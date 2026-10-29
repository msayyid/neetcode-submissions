class Solution:
    def maxArea(self, heights: List[int]) -> int:
        total = 0
        for i in range(len(heights)):
            for j in range(len(heights)):
                if i != j:
                    area = min(heights[i], heights[j]) * abs(j - i)
                    if area > total:
                        total = area
        return total
