# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        cur = root
        last_visited = None
        res = []

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            if stack[-1].right and stack[-1].right != last_visited:
                cur = stack[-1].right

            else:
                last_visited = stack.pop()
                res.append(last_visited.val)
        return res