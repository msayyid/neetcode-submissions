# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder = node - left - right
        # inorder = left - node - right

        root = TreeNode(preorder[0])
        stack = []
        stack.append(root)
        i = 0

        for val in preorder[1:]:
            node = TreeNode(val)
            
            if stack and stack[-1].val != inorder[i]:
                # we keep attaching left nodes
                stack[-1].left = node
                stack.append(node)
            else:
                while stack and stack[-1].val == inorder[i]:
                    i += 1
                    last_popped = stack.pop()

                last_popped.right = node
                stack.append(node)
        return root