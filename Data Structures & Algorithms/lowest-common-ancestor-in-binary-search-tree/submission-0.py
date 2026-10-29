# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if node.val < p.val and node.val < q.val:
                node = node.right
                stack.append(node)

            elif node.val > p.val and node.val > q.val:
                node = node.left
                stack.append(node)

            else:
                return node
            