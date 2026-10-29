# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = []
        last_visited = None

        cur = root
        heights = {}
        diameter = 0
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            node = stack[-1]
            if node.right and node.right != last_visited:
                cur = node.right

            else:
                last_visited = stack.pop()

                if last_visited.left:
                    left_height = heights[last_visited.left]

                else:
                    left_height = 0

                if last_visited.right:
                    right_height = heights[last_visited.right]

                else:
                    right_height = 0

                diameter = max(diameter, left_height + right_height)
                heights[last_visited] = 1 + max(left_height, right_height)

        return diameter