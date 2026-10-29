# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # find the node to delete and keep track of its parent
        cur = root
        parent = None
        while cur:
            if cur.val < key:
                parent = cur
                cur = cur.right

            elif cur.val > key:
                parent = cur
                cur = cur.left
            else:
                break

        # the node not found, doesn't exist
        if not cur:
            return root

        # special case, when root itself is the node to be deleted
        # and the root only has 0 or 1 child
        # there is no parent to reconnect, so its child
        # (or None if it is a leaf) becomes the new root
        if parent is None and not (cur.left and cur.right):
            return cur.left if cur.left else cur.right

        # case 1 - the node has no children at all
        # disconnect cur from its parent
        if not cur.left and not cur.right:
            if parent.left == cur:
                parent.left = None
            else:
                parent.right = None
            return root

        # case 2 - the node has only one child
        # skip cur and connect its parent directly to its child
        if (cur.left and not cur.right) or (not cur.left and cur.right):
            # find the only child of the cur
            if cur.left:
                child = cur.left
            else:
                child = cur.right
            
            # now find which child the cur is to the parent
            # reconnect the correct side of the parent
            if parent.left == cur:
                parent.left = child
            else:
                parent.right = child
            return root


        # case 3 - the node has two children
        # find the successor since we cannot just remove
        # we have to bring the right successor in place of the node
        # successor = the smallest node in cur's right subtree
        successor = cur.right
        parent_successor = cur
        while successor.left:
            parent_successor = successor
            successor = successor.left
        
        # now successor is found 
        # copy its value to the cur, not the whole node
        cur.val = successor.val


        # now remove the successor's original node, since it is 
        # no longer needed

        # since successor is the leftmost node in the right subtree,
        # it cannot have a left child
        # it can only have no child or a right child
        # make its parent skip successor and point to successor.right

        if parent_successor.left == successor:
            parent_successor.left = successor.right
        else:
            # cur.right itself was the inorder successor,
            # so successor is parent_successor's right child
            parent_successor.right = successor.right

        return root






















