# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder = node - left - right
        # inorder = left - node - right

        root = TreeNode(preorder[0])
        i = 0
        stack = []
        stack.append(root)

        for val in preorder[1:]:
            node = TreeNode(val)
            
            if stack[-1].val != inorder[i]:
                # if stack top is not equal to the inorder[i]
                # this means we are not done with the left subtree
                # of the current stack top, so we will keep
                # attaching to the left of of the stack top
                stack[-1].left = node
                stack.append(node)

            else:
                # now is the time to pop, since inorder[i] == stack top
                # this means left subtree of the current stack top
                # is finished, so we need to either go right 
                # or climb up
                while stack and stack[-1].val == inorder[i]:
                    last_popped = stack.pop()
                    i += 1
                
                last_popped.right = node
                stack.append(node)
        return root