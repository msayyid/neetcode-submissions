# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        stack = []
        root = TreeNode(preorder[0])
        stack.append(root)
        i = 0 # pointer for inorder list, to check if are done with the left
              # of side of the current node (stack top)
        # last_visited = None
        for val in preorder[1:]:
            node = TreeNode(val)

            # check if node needs to be attached
            if stack[-1].val != inorder[i]:
                # this means we are not done with 
                # the left of the node (stack top)
                stack[-1].left = node
                stack.append(node)

            # now, stack top matches with inorder[i], 
            # this means we are done with the left side of the stack top
            # we need to decide whether to go right or go up
            else:
                # last_visited = stack.pop()

                while stack and stack[-1].val == inorder[i]:
                    last_visited = stack.pop()
                    i += 1

                last_visited.right = node
                stack.append(node)
        return root
