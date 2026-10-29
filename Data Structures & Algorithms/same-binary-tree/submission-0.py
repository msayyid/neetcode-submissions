# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def same(node1, node2):
            if not node1 and not node2:
                return True

            if (not node1 and node2) or (node1 and not node2):
                return False

            if node1.val != node2.val:
                return False

            res1 = same(node1.left, node2.left)
            res2 = same(node1.right, node2.right)

            return res1 and res2
            # return same(node1.left, node2.left) 
        return same(p, q)