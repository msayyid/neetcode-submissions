# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur.right)
                res.append(cur.val)
                cur = cur.left
            # else:
            cur = stack.pop()
                # cur = cur.left
        return res