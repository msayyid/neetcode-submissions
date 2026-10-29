# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # we need postorder traversal

        stack = []
        cur = root
        last_visited = None
        heights = {}

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            if stack[-1].right and stack[-1].right != last_visited:
                cur = stack[-1].right

            else:
                last_visited = stack.pop()

                left_height = heights.get(last_visited.left, 0)
                right_height = heights.get(last_visited.right, 0)

                if abs(left_height - right_height) > 1:
                    return False

                heights[last_visited] = 1 + max(left_height, right_height)

        return True