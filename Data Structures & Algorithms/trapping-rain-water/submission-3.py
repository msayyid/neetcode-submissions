class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        left_max = [0] * n
        right_max = [0] * n
        
        # fill left_max
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])
        
        # fill right_max
        right_max[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])
        
        # calculate water
        water = 0
        for i in range(n):
            water += min(left_max[i], right_max[i]) - height[i]
        
        return water



# class Solution:
#     def trap(self, height: List[int]) -> int:
#         blocks = 0
#         i, j = 0, 1
#         n = len(height)
#         area = 0
#         max_wall = 0
#         blocks_up_to_max = 0
#         while i < n - 1:
#             if height[i] != 0 :
#                 blocks = 0 
#                 max_wall = 0
#                 max_wall_idx = 0
#                 blocks_up_to_max = 0
#                 while j < n and height[j] < height[i]:
#                     blocks += height[j]
                    
#                     if height[j] > max_wall:
#                         max_wall = height[j]
#                         max_wall_idx = j
#                         blocks_up_to_max = blocks
#                 if j == n:
#                     if max_wall == 0:
#                         break
#                     area += (min(max_wall, height[i]) * (max_wall_idx - i)) - blocks_up_to_max
#                     i = max_wall_idx
#                     j = i + 1
             
                          
#                 else:
#                     area += (min(height[j], height[i]) * (j - i)) - blocks
#                     i = j
#                     j = i + 1
#             else: 
#                 i += 1
#                 j = i + 1
        
#         return area
        
    


                
