# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # bfs through the nodes, find a potential
        # root of a subRoot, do dfs on it

        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node.val == subRoot.val:
                # start dfs in here
                stack = []
                stack.append((node, subRoot))
                same = True
                while stack:
                    node1, node2 = stack.pop()
                    if not node1 and not node2:
                        continue

                    if (not node1 and node2) or (node1 and not node2):
                        same = False
                        # return False
                        break

                    if node1.val != node2.val:
                        same = False
                        # return False
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
                