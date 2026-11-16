# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        stack = []
        cur = root
        prev = None
        while cur:
            if cur.val < key:
                prev = cur
                cur = cur.right
            elif cur.val > key:
                prev = cur
                cur = cur.left
            else:
                break
        if not cur:
            return root

        # special case if key is the root and if the root has only one child
        
        if not prev and not (root.left and root.right):
            if root.left:
                return root.left
            else:
                return root.right

        
        # case 1: the node has no children
        if not cur.left and not cur.right:
            if cur == prev.left:
                prev.left = None
            else:
                prev.right = None
            return root

        # case 2: the node has 1 child only
        if (cur.left and not cur.right) or (not cur.left and cur.right):
            if cur.left:
                child = cur.left
            else:
                child = cur.right
            
            if prev.left == cur:
                prev.left = child
            else:
                prev.right = child
            return root

        # case 3: the node has both children
        # find the successor
        # smallest node in the right subtree is a 
        # valid successor for us
        parent = cur
        successor = cur.right
        while successor.left:
            parent = successor
            successor = successor.left
        
        # now successor is found
        cur.val = successor.val
        # now remove the original successor
        if parent.left == successor:
            parent.left = successor.right
        else:
            parent.right = successor.right
        return root
        

