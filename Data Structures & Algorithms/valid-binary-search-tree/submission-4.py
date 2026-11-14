# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # inorder in bst gives us a sorted list of values

        stack = []
        cur = root
        prev = None
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            if prev:
                if cur.val <= prev.val:
                    return False
            prev = cur
            cur = cur.right
        return True