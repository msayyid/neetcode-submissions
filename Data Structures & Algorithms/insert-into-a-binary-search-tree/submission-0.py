# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        cur = root
        while cur:
            prev = cur
            if cur.val < val:
                cur = cur.right

            else:
                cur = cur.left

        
        new_node = TreeNode(val)
        if prev.val < val:
            prev.right = new_node

        else:
            prev.left = new_node

        return root