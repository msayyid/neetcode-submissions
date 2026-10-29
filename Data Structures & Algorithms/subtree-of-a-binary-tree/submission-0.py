# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # i want to try bfs
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node.val == subRoot.val:
                stack = []
                stack.append((node, subRoot))
                same = True
                while stack:
                    node1, node2 = stack.pop()
                    if not node1 and not node2:
                        continue
                        # break
                    if (not node1 and node2) or (node1 and not node2):
                        # continue
                        same = False
                        break

                    if node1.val != node2.val:
                        same = False
                        break

                    stack.append((node1.left, node2.left))
                    stack.append((node1.right, node2.right))
                if same:
                    return True

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        return False