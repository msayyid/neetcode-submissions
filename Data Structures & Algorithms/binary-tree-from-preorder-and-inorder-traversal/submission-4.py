# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder = node - left - right
        # inorder = left - node - right
        stack = []
        root = TreeNode(preorder[0])
        stack.append(root)
        i = 0

        for val in preorder[1:]:
            node = TreeNode(val)

            # if we have not reached the stack top in the inorder
            # we have not finished the left side of the stack top
            # so keep attaching to the left
            if stack[-1].val != inorder[i]:
                stack[-1].left = node
                stack.append(node)

            # now we are done with the left side of the current stack top
            # it is time to go either right or up
            else:
                while stack and stack[-1].val == inorder[i]:
                    last_popped = stack.pop()
                    i += 1

                # The LAST popped node is the highest ancestor
                # we've just finished moving past in inorder.
                #
                # Since preorder visits Root -> Left -> Right,
                # the next node must begin this ancestor's
                # right subtree.
                #
                # If another ancestor also needed to be completed,
                # the while loop would have continued popping.
                last_popped.right = node
                stack.append(node)
        return root