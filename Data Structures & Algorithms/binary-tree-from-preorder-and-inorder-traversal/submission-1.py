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
        stack = []
        stack.append(root)
        # stack keeps track of nodes that need their right child attached
        # and it is basically our current path

        i = 0
        # this is a pointer for inorder list, for us to detect
        # when we finished the left subtree, and when we need to 
        # go right or go upwards

        for val in preorder[1:]:
            node = TreeNode(val)

            if stack[-1].val != inorder[i]:
                # this means we are still on the left subtree of
                # the stack top node, so we keep attaching
                stack[-1].left = node
                stack.append(node)

            else:
                # now this means the stack top and inorder[i] match
                # meaning we need to decide whether to turn right or 
                # keep going up
                while stack and stack[-1].val == inorder[i]:
                    last_popped = stack.pop()
                    i += 1
                    # each pop means the node's left finished
                    # and we should either go up or go left
                    # no more left node will be attached to it
                    # and we move i, because we are done with the current 
                    # inorder[i] i guess ( i m not sure in here)

                # now we are done with the left
                # so we attach the node to the right of the most recent 
                # popped node because it is the node whose left is finished
                # and we start going deep (building its right subtree)??? i need help in here
                last_popped.right = node
                stack.append(node)
        return root