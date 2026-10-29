class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        n = len(height)
        water = 0
        for i in range(n):
            left_max = height[i]
            right_max = height[i]
            for j in range(i):
                left_max = max(left_max, height[j])
            for j in range(i + 1, n):
                right_max = max(right_max, height[j])
            water += min(left_max, right_max) - height[i]
        return water