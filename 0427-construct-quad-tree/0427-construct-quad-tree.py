"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def Helper(grid, x, y, n)->bool:
            val = grid[x][y]
            for i in range(x, x+n):
                for j in range(y, y+n):
                    if grid[i][j]!=val:
                        return False
            return True



        def solve(grid, x, y, n):
            if (Helper(grid, x, y, n)):
                return Node(grid[x][y], isLeaf = 1)
            
            root = Node(val = 1, isLeaf = 0)
            root.topLeft = solve(grid, x, y, n//2)
            root.topRight = solve(grid, x, y+(n//2), n//2)
            root.bottomLeft = solve(grid, x+(n//2), y, n//2)
            root.bottomRight = solve(grid, x+(n//2), y+(n//2), n//2)

            return root
        
        return solve(grid, 0, 0, len(grid))
            
        