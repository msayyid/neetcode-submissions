# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # LEFT -> RIGHT -> NODE

        stack = []
        res = []

        cur = root
        last_visited = None

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            node = stack[-1]
            # check if there's a right child to the current node
            # since children must be processed first
            if node.right and node.right != last_visited:
                cur = node.right
            
            else:
                last_visited = stack.pop()
                res.append(last_visited.val)

        return res