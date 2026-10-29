# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        counter = 0

        stack = []
        stack.append((root, root.val))

        while stack:
            node, max_val_so_far = stack.pop()

            if node.val >= max_val_so_far:
                counter += 1

            if node.left:
                stack.append((node.left, max(node.left.val, max_val_so_far)))
            
            if node.right:
                stack.append((node.right, max(node.right.val, max_val_so_far)))

        return counter
        