# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # postorder = left - right - node
        stack = []
        last_visited = None
        cur = root
        res = []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            node = stack[-1]
            if node.right and last_visited != node.right:
                cur = node.right
            else:
                last_visited = stack.pop()
                res.append(last_visited.val)
        return res