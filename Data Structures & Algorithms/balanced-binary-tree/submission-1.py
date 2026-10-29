# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # we will be doing dfs postorder 
        stack = []

        last_visited = None
        cur = root
        heights = {}
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            # no more left is possible, check right if possible keep going left
            node = stack[-1]
            if node.right and node.right != last_visited:
                cur = node.right

            else:
                # we are as deep as possible
                # so we will be processing the nodes in here

                last_visited = stack.pop()

                # get the heights of left and right sides of the last_visited
                left_side = heights.get(last_visited.left, 0)
                right_side = heights.get(last_visited.right, 0)

                # check the difference
                if abs(left_side - right_side) > 1:
                    return False

                heights[last_visited] = 1 + max(left_side, right_side)
        return True
