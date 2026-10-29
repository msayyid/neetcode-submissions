# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # bfs through the main tree to find possible starting nodes
        q = deque()
        q.append(root)

        while q:
            node = q.popleft()

            # matching value only means this node is a possible candidate
            if node.val == subRoot.val:
                # iterative same tree check using a stack of node pairs
                stack = []
                stack.append((node, subRoot))
                same = True
                while stack:
                    node1, node2 = stack.pop()
                    # both missing at the same position -> still matching
                    if not node1 and not node2:
                        continue

                    # structure differs -> candidate subtree does not match
                    if (not node1 and node2) or (node1 and not node2):
                        same = False
                        break

                    # values differ -> candidate subtree does not match
                    if node1.val != node2.val:
                        same = False
                        break

                    # compare corresponding left and right children
                    stack.append((node1.left, node2.left))
                    stack.append((node1.right, node2.right))

                # entire subtree matched
                if same:
                    return True

            # continue bfs through the main tree
            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        return False

# BFS through root
# → find candidate by value
# → run iterative Same Tree check
# → if fully identical, return True