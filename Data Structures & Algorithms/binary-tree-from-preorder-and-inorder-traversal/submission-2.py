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
        # stack stores the current path of nodes
        # whose traversal/building is not fully finished yet

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
                    # each pop means the node's left is finished
                    # and we are climbing up to see whether an ancestor
                    # is also finished with its left subtree
                    # and we move i += 1, meaning i have finished dealing 
                    # with this inorder node; move to the next inorder position

                # after popping all nodes whose left subtree is finished,
                # last_popped is the node from which we now need to turn right
                # 
                # preorder is NODE - LEFT - RIGHT,
                # so the current preorder node starts last_popped's right subtree
                last_popped.right = node
                stack.append(node)
        return root