"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        rows = len(grid)
        root = Node(False, False, None, None, None, None)
        stack = []

        # stack's entry:
        # (node, top left row, top left column, size of the region)
        stack.append((root, 0, 0, rows))

        while stack:
            node, row, col, size = stack.pop()
            first = grid[row][col]
            same = True
            # check if the region is uniform
            for r in range(row, row + size):
                for c in range(col, col + size):
                    if grid[r][c] != first:
                        same = False
                        break

                if not same:
                    break
            
            # if the region is only 1s or only 0s
            if same:
                # mark it a leaf and set its value
                node.isLeaf = True
                node.val = bool(first)

            else:
                # if not uniform
                # split into 4 regions and send to the stack
                node.topLeft = Node(False, False, None, None, None, None)
                node.topRight = Node(False, False, None, None, None, None)
                node.bottomLeft = Node(False, False, None, None, None, None)
                node.bottomRight = Node(False, False, None, None, None, None)

                half = size // 2
                stack.append((node.topLeft, row, col, half))
                stack.append((node.topRight, row, col + half, half))
                stack.append((node.bottomLeft, row + half, col, half))
                stack.append((node.bottomRight, row + half, col + half, half))
        return root