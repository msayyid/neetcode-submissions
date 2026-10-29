class Solution:
    def trap(self, height: List[int]) -> int:
        blocks = 0
        i, j = 0, 1
        n = len(height)
        area = 0
        max_wall = 0
        blocks_up_to_max = 0
        while i < n - 1:
            if height[i] != 0 :
                blocks = 0 
                max_wall = 0
                max_wall_idx = 0
                blocks_up_to_max = 0
                while j < n and height[j] < height[i]:
                    blocks += height[j]
                    
                    if height[j] > max_wall:
                        max_wall = height[j]
                        max_wall_idx = j
                        blocks_up_to_max = blocks
                if j == n:
                    if max_wall == 0:
                        break
                    area += (min(max_wall, height[i]) * (max_wall_idx - i)) - blocks_up_to_max
                    i = max_wall_idx
                    j = i + 1
             
                          
                else:
                    area += (min(height[j], height[i]) * (j - i)) - blocks
                    i = j
                    j = i + 1
            else: 
                i += 1
                j -= 1
        
        return area
        
    


                
