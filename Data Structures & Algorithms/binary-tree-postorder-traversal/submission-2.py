# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # LEFT -> RIGHT -> NODE
        stack = []
        res = []
        last_seen = None
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            node = stack[-1]
            if node.right and node.right != last_seen:
                cur = node.right

            else:
                last_seen = stack.pop()
                res.append(last_seen.val)

            # cur = cur.right

        return res